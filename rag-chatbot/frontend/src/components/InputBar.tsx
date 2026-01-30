import { useState, useRef, useEffect } from 'react';

interface InputBarProps {
  onSendMessage: (message: string) => void;
  isLoading: boolean;
  onClearChat: () => void;
  hasMessages: boolean;
}

function InputBar({ onSendMessage, isLoading, onClearChat, hasMessages }: InputBarProps) {
  const [input, setInput] = useState('');
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  useEffect(() => {
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
      textareaRef.current.style.height = `${textareaRef.current.scrollHeight}px`;
    }
  }, [input]);

  const handleSubmit = (e?: React.FormEvent) => {
    e?.preventDefault();
    if (input.trim() && !isLoading) {
      onSendMessage(input);
      setInput('');
      if (textareaRef.current) {
        textareaRef.current.style.height = 'auto';
      }
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  };

  return (
    <div className="space-y-3">
      <div className="relative">
        <textarea
          ref={textareaRef}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Ask anything..."
          disabled={isLoading}
          className="w-full bg-chat-tertiary border border-chat-border rounded-3xl px-6 py-4 pr-14 text-gray-200 placeholder-gray-500 focus:outline-none focus:border-gray-600 resize-none transition-all disabled:opacity-50 disabled:cursor-not-allowed shadow-lg"
          rows={1}
          style={{ maxHeight: '200px' }}
        />

        <button
          onClick={() => handleSubmit()}
          disabled={!input.trim() || isLoading}
          className="absolute right-3 bottom-3 w-10 h-10 rounded-full bg-gray-200 hover:bg-gray-300 disabled:bg-gray-700 disabled:cursor-not-allowed flex items-center justify-center transition-colors group"
        >
          <svg
            className="w-5 h-5 text-gray-900 group-disabled:text-gray-500"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M5 10l7-7m0 0l7 7m-7-7v18"
            />
          </svg>
        </button>
      </div>

      {hasMessages && (
        <button
          onClick={onClearChat}
          className="text-sm text-gray-400 hover:text-gray-300 transition-colors"
        >
          Clear conversation
        </button>
      )}
    </div>
  );
}

export default InputBar;
