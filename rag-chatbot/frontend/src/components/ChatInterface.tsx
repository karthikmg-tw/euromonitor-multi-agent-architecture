import { useState, useRef, useEffect } from 'react';
import { ChatMessage, sendMessage, Source } from '../services/api';
import MessageList from './MessageList';
import InputBar from './InputBar';

const EXAMPLE_QUESTIONS = [
  "What is driving growth in the Asia Pacific toys market?",
  "Tell me about the kidults consumer segment",
  "What trends are affecting traditional toys and games?",
  "How is China's toys and games market performing?"
];

export interface Message extends ChatMessage {
  sources?: Source[];
}

function ChatInterface() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [topK, setTopK] = useState(5);
  const [minSimilarity, setMinSimilarity] = useState(0.05);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSendMessage = async (content: string) => {
    if (!content.trim() || isLoading) return;

    // Add user message
    const userMessage: Message = { role: 'user', content };
    setMessages((prev) => [...prev, userMessage]);
    setIsLoading(true);

    try {
      const response = await sendMessage(content, topK, minSimilarity);

      // Add assistant message with sources
      const assistantMessage: Message = {
        role: 'assistant',
        content: response.answer,
        sources: response.sources
      };
      setMessages((prev) => [...prev, assistantMessage]);
    } catch (error) {
      const errorMessage: Message = {
        role: 'assistant',
        content: error instanceof Error ? error.message : 'An error occurred'
      };
      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleExampleClick = (question: string) => {
    handleSendMessage(question);
  };

  const handleClearChat = () => {
    setMessages([]);
  };

  return (
    <div className="flex flex-col h-full">
      {/* Messages Area */}
      <div className="flex-1 overflow-y-auto">
        {messages.length === 0 ? (
          <div className="flex flex-col items-center justify-center h-full px-4">
            <h2 className="text-3xl font-medium text-gray-200 mb-12">Ready when you are.</h2>

            {/* Example Questions */}
            <div className="w-full max-w-3xl grid grid-cols-1 md:grid-cols-2 gap-3 mb-8">
              {EXAMPLE_QUESTIONS.map((question, index) => (
                <button
                  key={index}
                  onClick={() => handleExampleClick(question)}
                  disabled={isLoading}
                  className="text-left p-4 rounded-xl bg-chat-tertiary border border-chat-border hover:bg-chat-secondary hover:border-gray-600 transition-all text-gray-300 text-sm disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  {question}
                </button>
              ))}
            </div>
          </div>
        ) : (
          <>
            <MessageList messages={messages} isLoading={isLoading} />
            <div ref={messagesEndRef} />
          </>
        )}
      </div>

      {/* Input Area */}
      <div className="border-t border-chat-border p-4">
        <div className="max-w-3xl mx-auto">
          <InputBar
            onSendMessage={handleSendMessage}
            isLoading={isLoading}
            onClearChat={handleClearChat}
            hasMessages={messages.length > 0}
          />

          {/* Settings - Collapsible */}
          <details className="mt-4">
            <summary className="cursor-pointer text-gray-400 text-sm hover:text-gray-300">
              ⚙️ Settings
            </summary>
            <div className="mt-3 p-4 bg-chat-tertiary rounded-lg space-y-4">
              <div>
                <label className="block text-sm text-gray-300 mb-2">
                  Number of sources: {topK}
                </label>
                <input
                  type="range"
                  min="1"
                  max="10"
                  value={topK}
                  onChange={(e) => setTopK(Number(e.target.value))}
                  className="w-full accent-chat-accent"
                />
              </div>
              <div>
                <label className="block text-sm text-gray-300 mb-2">
                  Relevance threshold: {minSimilarity.toFixed(2)}
                </label>
                <input
                  type="range"
                  min="0"
                  max="1"
                  step="0.05"
                  value={minSimilarity}
                  onChange={(e) => setMinSimilarity(Number(e.target.value))}
                  className="w-full accent-chat-accent"
                />
              </div>
            </div>
          </details>
        </div>
      </div>
    </div>
  );
}

export default ChatInterface;
