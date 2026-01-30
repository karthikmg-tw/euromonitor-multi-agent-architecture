import { Message } from './ChatInterface';

interface MessageListProps {
  messages: Message[];
  isLoading: boolean;
}

function MessageList({ messages, isLoading }: MessageListProps) {
  return (
    <div className="max-w-3xl mx-auto px-4 py-8 space-y-6">
      {messages.map((message, index) => (
        <div key={index} className="space-y-4">
          <div className={`${message.role === 'user' ? 'bg-chat-secondary rounded-2xl p-4' : ''}`}>
            <div className="flex items-start gap-4">
              {message.role === 'assistant' && (
                <div className="w-8 h-8 rounded-full bg-chat-accent flex items-center justify-center flex-shrink-0">
                  <svg className="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
                  </svg>
                </div>
              )}
              {message.role === 'user' && (
                <div className="w-8 h-8 rounded-full bg-gray-600 flex items-center justify-center flex-shrink-0 text-white font-semibold text-sm">
                  U
                </div>
              )}
              <div className="flex-1 pt-1">
                <div className="text-gray-200 markdown-content">
                  {message.content}
                </div>

                {/* Sources */}
                {message.sources && message.sources.length > 0 && (
                  <div className="mt-6 pt-6 border-t border-chat-border">
                    <h4 className="text-sm font-semibold text-gray-300 mb-3">📚 Sources</h4>
                    <div className="space-y-3">
                      {message.sources.map((source, idx) => (
                        <div key={idx} className="bg-chat-tertiary border border-chat-border rounded-lg p-3">
                          <div className="font-medium text-gray-200 text-sm mb-1">
                            {idx + 1}. {source.label}
                          </div>
                          <div className="text-xs inline-block px-2 py-0.5 bg-chat-accent text-white rounded mb-2">
                            {source.type}
                          </div>
                          <div className="text-gray-400 text-sm mb-2 leading-relaxed">
                            {source.description}
                          </div>
                          <div className="text-chat-accent text-xs font-mono">
                            🔗 {source.source_urls}
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      ))}

      {isLoading && (
        <div className="flex items-start gap-4">
          <div className="w-8 h-8 rounded-full bg-chat-accent flex items-center justify-center flex-shrink-0">
            <svg className="w-5 h-5 text-white animate-spin" fill="none" viewBox="0 0 24 24">
              <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
              <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
          </div>
          <div className="flex-1 pt-1">
            <div className="flex gap-1">
              <div className="w-2 h-2 bg-gray-500 rounded-full animate-bounce" style={{ animationDelay: '0ms' }}></div>
              <div className="w-2 h-2 bg-gray-500 rounded-full animate-bounce" style={{ animationDelay: '150ms' }}></div>
              <div className="w-2 h-2 bg-gray-500 rounded-full animate-bounce" style={{ animationDelay: '300ms' }}></div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default MessageList;
