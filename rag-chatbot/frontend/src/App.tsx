import { useState, useRef, useEffect } from 'react';
import axios from 'axios';

const API_URL = 'http://localhost:8000';

interface Source {
  entity_id: string;
  label: string;
  type: string;
  description: string;
  source_urls: string;
}

interface Message {
  role: 'user' | 'assistant';
  content: string;
  sources?: Source[];
  sourcesExpanded?: boolean;
}

function App() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const [backendHealth, setBackendHealth] = useState<boolean | null>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  // Check backend health
  useEffect(() => {
    const checkHealth = async () => {
      try {
        const response = await axios.get(`${API_URL}/health`, { timeout: 5000 });
        setBackendHealth(response.status === 200);
      } catch {
        setBackendHealth(false);
      }
    };
    checkHealth();
    const interval = setInterval(checkHealth, 30000);
    return () => clearInterval(interval);
  }, []);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  useEffect(() => {
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
      textareaRef.current.style.height = textareaRef.current.scrollHeight + 'px';
    }
  }, [input]);

  const toggleSources = (index: number) => {
    setMessages(prev => prev.map((msg, i) =>
      i === index ? { ...msg, sourcesExpanded: !msg.sourcesExpanded } : msg
    ));
  };

  const handleSend = async () => {
    if (!input.trim() || isTyping) return;

    const userMessage: Message = { role: 'user', content: input };
    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setIsTyping(true);

    try {
      const response = await axios.post(`${API_URL}/chat`, {
        query: input,
        top_k: 5,
        include_relationships: true,
        min_similarity: 0.05,
        debug: false
      }, {
        timeout: 30000
      });

      const assistantMessage: Message = {
        role: 'assistant',
        content: response.data.answer,
        sources: response.data.sources,
        sourcesExpanded: false
      };
      setMessages(prev => [...prev, assistantMessage]);
    } catch (error) {
      let errorMessage = 'An error occurred while processing your request.';

      if (axios.isAxiosError(error)) {
        if (error.code === 'ECONNABORTED') {
          errorMessage = '⏱️ Request timed out. Please try again.';
        } else if (error.code === 'ERR_NETWORK') {
          errorMessage = '🔌 Cannot connect to backend. Please ensure the server is running on port 8000.';
        } else if (error.response) {
          errorMessage = `❌ ${error.response.data.detail || 'Server error occurred'}`;
        }
      }

      setMessages(prev => [...prev, {
        role: 'assistant',
        content: errorMessage
      }]);
    } finally {
      setIsTyping(false);
    }
  };

  const examples = [
    "What is driving growth in the Asia Pacific toys market?",
    "Tell me about the kidults consumer segment",
    "What trends are affecting traditional toys?",
    "How is China's toys and games market performing?"
  ];

  return (
    <div style={{
      height: '100vh',
      width: '100vw',
      display: 'flex',
      overflow: 'hidden',
      background: 'linear-gradient(135deg, #1a1a1a 0%, #1e1e1e 100%)',
      fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
    }}>
      {/* Sidebar */}
      <div style={{
        width: '260px',
        background: 'linear-gradient(180deg, #212121 0%, #1a1a1a 100%)',
        borderRight: '1px solid rgba(255, 255, 255, 0.08)',
        display: 'flex',
        flexDirection: 'column',
        boxShadow: '2px 0 12px rgba(0, 0, 0, 0.3)',
        transition: 'all 0.3s ease'
      }}>
        {/* Header */}
        <div style={{ padding: '20px', borderBottom: '1px solid rgba(255, 255, 255, 0.08)' }}>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
            <div>
              <h1 style={{
                fontSize: '18px',
                fontWeight: '600',
                background: 'linear-gradient(135deg, #10b981 0%, #059669 100%)',
                WebkitBackgroundClip: 'text',
                WebkitTextFillColor: 'transparent',
                letterSpacing: '-0.02em'
              }}>
                Market Research AI
              </h1>
              <p style={{ fontSize: '12px', color: '#666', marginTop: '4px' }}>
                Asia Pacific Insights
              </p>
            </div>
            <div style={{
              width: '10px',
              height: '10px',
              borderRadius: '50%',
              background: backendHealth ? '#10b981' : '#ef4444',
              boxShadow: `0 0 10px ${backendHealth ? '#10b981' : '#ef4444'}`,
              animation: 'pulse 2s ease-in-out infinite'
            }} />
          </div>
        </div>

        {/* New Chat Button */}
        <div style={{ padding: '16px' }}>
          <button
            onClick={() => setMessages([])}
            style={{
              width: '100%',
              padding: '12px 16px',
              background: 'rgba(16, 185, 129, 0.1)',
              border: '1px solid rgba(16, 185, 129, 0.2)',
              borderRadius: '12px',
              color: '#10b981',
              fontSize: '14px',
              fontWeight: '500',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '10px',
              transition: 'all 0.2s ease'
            }}
            onMouseEnter={(e) => {
              e.currentTarget.style.background = 'rgba(16, 185, 129, 0.15)';
              e.currentTarget.style.transform = 'translateY(-1px)';
            }}
            onMouseLeave={(e) => {
              e.currentTarget.style.background = 'rgba(16, 185, 129, 0.1)';
              e.currentTarget.style.transform = 'translateY(0)';
            }}
          >
            <span style={{ fontSize: '18px' }}>✨</span>
            <span>New Chat</span>
          </button>
        </div>

        {/* Spacer */}
        <div style={{ flex: 1 }} />

        {/* Footer */}
        <div style={{
          padding: '16px',
          borderTop: '1px solid rgba(255, 255, 255, 0.08)',
          background: 'rgba(0, 0, 0, 0.2)'
        }}>
          <div style={{
            display: 'flex',
            alignItems: 'center',
            gap: '12px',
            padding: '10px',
            borderRadius: '10px'
          }}>
            <div style={{
              width: '36px',
              height: '36px',
              borderRadius: '50%',
              background: 'linear-gradient(135deg, #10b981 0%, #059669 100%)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontSize: '16px',
              fontWeight: '600',
              color: 'white',
              boxShadow: '0 2px 8px rgba(16, 185, 129, 0.3)'
            }}>
              U
            </div>
            <div>
              <div style={{ fontSize: '14px', color: '#e5e5e5', fontWeight: '500' }}>User</div>
              <div style={{ fontSize: '12px', color: '#666' }}>
                {backendHealth ? '🟢 Connected' : '🔴 Offline'}
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', position: 'relative' }}>
        {/* Messages Area */}
        <div style={{
          flex: 1,
          overflowY: 'auto',
          padding: '24px',
          scrollBehavior: 'smooth'
        }}>
          {messages.length === 0 ? (
            <div style={{
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              justifyContent: 'center',
              height: '100%',
              animation: 'fadeIn 0.6s ease'
            }}>
              <h2 style={{
                fontSize: '42px',
                fontWeight: '500',
                color: '#e5e5e5',
                marginBottom: '48px',
                letterSpacing: '-0.03em',
                animation: 'slideDown 0.6s ease'
              }}>
                Ready when you are.
              </h2>

              {/* Example Cards */}
              <div style={{
                width: '100%',
                maxWidth: '900px',
                display: 'grid',
                gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))',
                gap: '16px'
              }}>
                {examples.map((example, i) => (
                  <button
                    key={i}
                    onClick={() => {
                      setInput(example);
                      setTimeout(handleSend, 100);
                    }}
                    style={{
                      padding: '20px',
                      background: 'rgba(255, 255, 255, 0.03)',
                      border: '1px solid rgba(255, 255, 255, 0.08)',
                      borderRadius: '16px',
                      color: '#b4b4b4',
                      fontSize: '14px',
                      textAlign: 'left',
                      cursor: 'pointer',
                      transition: 'all 0.3s ease',
                      lineHeight: '1.5',
                      animation: `slideUp 0.6s ease ${i * 0.1}s both`
                    }}
                    onMouseEnter={(e) => {
                      e.currentTarget.style.background = 'rgba(255, 255, 255, 0.06)';
                      e.currentTarget.style.borderColor = 'rgba(16, 185, 129, 0.3)';
                      e.currentTarget.style.transform = 'translateY(-4px)';
                      e.currentTarget.style.boxShadow = '0 8px 24px rgba(0, 0, 0, 0.4)';
                    }}
                    onMouseLeave={(e) => {
                      e.currentTarget.style.background = 'rgba(255, 255, 255, 0.03)';
                      e.currentTarget.style.borderColor = 'rgba(255, 255, 255, 0.08)';
                      e.currentTarget.style.transform = 'translateY(0)';
                      e.currentTarget.style.boxShadow = 'none';
                    }}
                  >
                    {example}
                  </button>
                ))}
              </div>
            </div>
          ) : (
            <div style={{ maxWidth: '900px', margin: '0 auto' }}>
              {messages.map((msg, i) => (
                <div
                  key={i}
                  style={{
                    marginBottom: '32px',
                    animation: 'messageSlideIn 0.4s ease both',
                    animationDelay: `${i * 0.05}s`
                  }}
                >
                  <div style={{ display: 'flex', gap: '16px' }}>
                    <div style={{
                      width: '40px',
                      height: '40px',
                      borderRadius: '50%',
                      background: msg.role === 'user'
                        ? 'linear-gradient(135deg, #4b5563 0%, #374151 100%)'
                        : 'linear-gradient(135deg, #10b981 0%, #059669 100%)',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      fontSize: '16px',
                      fontWeight: '600',
                      color: 'white',
                      flexShrink: 0,
                      boxShadow: msg.role === 'assistant'
                        ? '0 4px 12px rgba(16, 185, 129, 0.3)'
                        : '0 2px 8px rgba(0, 0, 0, 0.3)'
                    }}>
                      {msg.role === 'user' ? 'U' : 'AI'}
                    </div>
                    <div style={{ flex: 1 }}>
                      <div style={{
                        paddingTop: '8px',
                        color: '#e5e5e5',
                        fontSize: '15px',
                        lineHeight: '1.7',
                        letterSpacing: '-0.01em',
                        whiteSpace: 'pre-wrap'
                      }}>
                        {msg.content}
                      </div>

                      {/* Sources Toggle Button */}
                      {msg.sources && msg.sources.length > 0 && (
                        <div style={{ marginTop: '16px' }}>
                          <button
                            onClick={() => toggleSources(i)}
                            style={{
                              padding: '8px 16px',
                              background: msg.sourcesExpanded
                                ? 'rgba(16, 185, 129, 0.15)'
                                : 'rgba(255, 255, 255, 0.05)',
                              border: `1px solid ${msg.sourcesExpanded
                                ? 'rgba(16, 185, 129, 0.3)'
                                : 'rgba(255, 255, 255, 0.1)'}`,
                              borderRadius: '8px',
                              color: msg.sourcesExpanded ? '#10b981' : '#b4b4b4',
                              fontSize: '13px',
                              fontWeight: '500',
                              cursor: 'pointer',
                              display: 'flex',
                              alignItems: 'center',
                              gap: '8px',
                              transition: 'all 0.2s ease'
                            }}
                            onMouseEnter={(e) => {
                              e.currentTarget.style.background = msg.sourcesExpanded
                                ? 'rgba(16, 185, 129, 0.2)'
                                : 'rgba(255, 255, 255, 0.08)';
                              e.currentTarget.style.transform = 'translateX(2px)';
                            }}
                            onMouseLeave={(e) => {
                              e.currentTarget.style.background = msg.sourcesExpanded
                                ? 'rgba(16, 185, 129, 0.15)'
                                : 'rgba(255, 255, 255, 0.05)';
                              e.currentTarget.style.transform = 'translateX(0)';
                            }}
                          >
                            <span style={{ fontSize: '16px' }}>
                              {msg.sourcesExpanded ? '📖' : '📚'}
                            </span>
                            <span>
                              {msg.sourcesExpanded ? 'Hide' : 'View'} {msg.sources.length} source{msg.sources.length !== 1 ? 's' : ''}
                            </span>
                            <span style={{
                              transition: 'transform 0.2s ease',
                              transform: msg.sourcesExpanded ? 'rotate(180deg)' : 'rotate(0deg)',
                              display: 'inline-block'
                            }}>
                              ▼
                            </span>
                          </button>

                          {/* Collapsible Sources */}
                          <div style={{
                            maxHeight: msg.sourcesExpanded ? '2000px' : '0',
                            overflow: 'hidden',
                            transition: 'max-height 0.4s ease, opacity 0.3s ease',
                            opacity: msg.sourcesExpanded ? 1 : 0
                          }}>
                            <div style={{
                              marginTop: '16px',
                              paddingTop: '16px',
                              borderTop: '1px solid rgba(255, 255, 255, 0.08)'
                            }}>
                              <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                                {msg.sources.map((source, j) => (
                                  <div
                                    key={j}
                                    style={{
                                      padding: '16px',
                                      background: 'rgba(255, 255, 255, 0.03)',
                                      border: '1px solid rgba(255, 255, 255, 0.08)',
                                      borderRadius: '12px',
                                      transition: 'all 0.2s ease',
                                      animation: `slideUp 0.3s ease ${j * 0.05}s both`
                                    }}
                                    onMouseEnter={(e) => {
                                      e.currentTarget.style.background = 'rgba(255, 255, 255, 0.05)';
                                      e.currentTarget.style.borderColor = 'rgba(16, 185, 129, 0.2)';
                                    }}
                                    onMouseLeave={(e) => {
                                      e.currentTarget.style.background = 'rgba(255, 255, 255, 0.03)';
                                      e.currentTarget.style.borderColor = 'rgba(255, 255, 255, 0.08)';
                                    }}
                                  >
                                    <div style={{
                                      fontSize: '14px',
                                      fontWeight: '500',
                                      color: '#e5e5e5',
                                      marginBottom: '8px'
                                    }}>
                                      {j + 1}. {source.label}
                                    </div>
                                    <div style={{
                                      display: 'inline-block',
                                      padding: '4px 10px',
                                      background: 'rgba(16, 185, 129, 0.15)',
                                      border: '1px solid rgba(16, 185, 129, 0.3)',
                                      borderRadius: '6px',
                                      fontSize: '11px',
                                      fontWeight: '600',
                                      color: '#10b981',
                                      textTransform: 'uppercase',
                                      letterSpacing: '0.5px',
                                      marginBottom: '10px'
                                    }}>
                                      {source.type}
                                    </div>
                                    <div style={{
                                      fontSize: '13px',
                                      color: '#b4b4b4',
                                      lineHeight: '1.6',
                                      marginBottom: '10px'
                                    }}>
                                      {source.description}
                                    </div>
                                    <div style={{
                                      fontSize: '12px',
                                      color: '#666',
                                      fontFamily: 'monospace'
                                    }}>
                                      🔗 {source.source_urls}
                                    </div>
                                  </div>
                                ))}
                              </div>
                            </div>
                          </div>
                        </div>
                      )}
                    </div>
                  </div>
                </div>
              ))}

              {isTyping && (
                <div style={{
                  display: 'flex',
                  gap: '16px',
                  marginBottom: '32px',
                  animation: 'fadeIn 0.3s ease'
                }}>
                  <div style={{
                    width: '40px',
                    height: '40px',
                    borderRadius: '50%',
                    background: 'linear-gradient(135deg, #10b981 0%, #059669 100%)',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    boxShadow: '0 4px 12px rgba(16, 185, 129, 0.3)'
                  }}>
                    <div style={{
                      width: '20px',
                      height: '20px',
                      border: '2px solid white',
                      borderTop: '2px solid transparent',
                      borderRadius: '50%',
                      animation: 'spin 0.8s linear infinite'
                    }} />
                  </div>
                  <div style={{ paddingTop: '12px', display: 'flex', gap: '6px' }}>
                    {[0, 1, 2].map((i) => (
                      <div
                        key={i}
                        style={{
                          width: '8px',
                          height: '8px',
                          borderRadius: '50%',
                          background: '#666',
                          animation: 'bounce 1.4s ease-in-out infinite',
                          animationDelay: `${i * 0.15}s`
                        }}
                      />
                    ))}
                  </div>
                </div>
              )}
              <div ref={messagesEndRef} />
            </div>
          )}
        </div>

        {/* Input Bar */}
        <div style={{
          padding: '24px',
          background: 'linear-gradient(180deg, transparent 0%, rgba(0, 0, 0, 0.3) 100%)',
          borderTop: '1px solid rgba(255, 255, 255, 0.08)'
        }}>
          <div style={{ maxWidth: '900px', margin: '0 auto', position: 'relative' }}>
            <textarea
              ref={textareaRef}
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === 'Enter' && !e.shiftKey) {
                  e.preventDefault();
                  handleSend();
                }
              }}
              placeholder="Ask anything..."
              disabled={isTyping || !backendHealth}
              rows={1}
              style={{
                width: '100%',
                minHeight: '56px',
                maxHeight: '200px',
                padding: '16px 60px 16px 24px',
                background: 'rgba(255, 255, 255, 0.05)',
                border: '1px solid rgba(255, 255, 255, 0.1)',
                borderRadius: '28px',
                color: '#e5e5e5',
                fontSize: '15px',
                resize: 'none',
                outline: 'none',
                transition: 'all 0.2s ease',
                boxShadow: '0 4px 16px rgba(0, 0, 0, 0.2)',
                fontFamily: 'inherit',
                lineHeight: '1.5',
                opacity: (!backendHealth || isTyping) ? 0.5 : 1
              }}
              onFocus={(e) => {
                if (backendHealth && !isTyping) {
                  e.target.style.background = 'rgba(255, 255, 255, 0.08)';
                  e.target.style.borderColor = 'rgba(16, 185, 129, 0.3)';
                  e.target.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.3), 0 0 0 3px rgba(16, 185, 129, 0.1)';
                }
              }}
              onBlur={(e) => {
                e.target.style.background = 'rgba(255, 255, 255, 0.05)';
                e.target.style.borderColor = 'rgba(255, 255, 255, 0.1)';
                e.target.style.boxShadow = '0 4px 16px rgba(0, 0, 0, 0.2)';
              }}
            />
            <button
              onClick={handleSend}
              disabled={!input.trim() || isTyping || !backendHealth}
              style={{
                position: 'absolute',
                right: '8px',
                bottom: '8px',
                width: '40px',
                height: '40px',
                borderRadius: '50%',
                background: (input.trim() && !isTyping && backendHealth)
                  ? 'linear-gradient(135deg, #10b981 0%, #059669 100%)'
                  : 'rgba(255, 255, 255, 0.1)',
                border: 'none',
                color: 'white',
                fontSize: '20px',
                cursor: (input.trim() && !isTyping && backendHealth) ? 'pointer' : 'not-allowed',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                transition: 'all 0.2s ease',
                boxShadow: (input.trim() && !isTyping && backendHealth)
                  ? '0 4px 12px rgba(16, 185, 129, 0.4)'
                  : 'none'
              }}
              onMouseEnter={(e) => {
                if (input.trim() && !isTyping && backendHealth) {
                  e.currentTarget.style.transform = 'scale(1.05)';
                  e.currentTarget.style.boxShadow = '0 6px 16px rgba(16, 185, 129, 0.5)';
                }
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.transform = 'scale(1)';
                e.currentTarget.style.boxShadow = (input.trim() && !isTyping && backendHealth)
                  ? '0 4px 12px rgba(16, 185, 129, 0.4)'
                  : 'none';
              }}
            >
              ↑
            </button>
          </div>
        </div>
      </div>

      {/* CSS Animations */}
      <style>{`
        @keyframes fadeIn {
          from { opacity: 0; }
          to { opacity: 1; }
        }

        @keyframes slideDown {
          from {
            opacity: 0;
            transform: translateY(-20px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }

        @keyframes slideUp {
          from {
            opacity: 0;
            transform: translateY(20px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }

        @keyframes messageSlideIn {
          from {
            opacity: 0;
            transform: translateX(-10px);
          }
          to {
            opacity: 1;
            transform: translateX(0);
          }
        }

        @keyframes bounce {
          0%, 80%, 100% { transform: translateY(0); }
          40% { transform: translateY(-8px); }
        }

        @keyframes spin {
          to { transform: rotate(360deg); }
        }

        @keyframes pulse {
          0%, 100% { opacity: 1; }
          50% { opacity: 0.5; }
        }

        ::placeholder {
          color: #666;
          opacity: 1;
        }

        ::-webkit-scrollbar {
          width: 8px;
        }

        ::-webkit-scrollbar-track {
          background: transparent;
        }

        ::-webkit-scrollbar-thumb {
          background: rgba(255, 255, 255, 0.1);
          border-radius: 4px;
        }

        ::-webkit-scrollbar-thumb:hover {
          background: rgba(255, 255, 255, 0.15);
        }
      `}</style>
    </div>
  );
}

export default App;
