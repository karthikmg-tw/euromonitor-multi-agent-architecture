import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

export interface ChatMessage {
  role: 'user' | 'assistant';
  content: string;
}

export interface Source {
  entity_id: string;
  label: string;
  type: string;
  description: string;
  source_urls: string;
}

export interface ChatResponse {
  answer: string;
  sources: Source[];
}

export const sendMessage = async (
  query: string,
  topK: number = 5,
  minSimilarity: number = 0.05
): Promise<ChatResponse> => {
  try {
    const response = await axios.post(`${API_BASE_URL}/chat`, {
      query,
      top_k: topK,
      include_relationships: true,
      min_similarity: minSimilarity,
      debug: false
    }, {
      timeout: 30000
    });

    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      if (error.code === 'ECONNABORTED') {
        throw new Error('Request timed out. Please try again.');
      }
      if (error.response) {
        throw new Error(error.response.data.detail || 'Server error occurred');
      }
      if (error.code === 'ERR_NETWORK') {
        throw new Error('Cannot connect to backend. Please ensure the server is running on port 8000.');
      }
    }
    throw new Error('An unexpected error occurred');
  }
};

export const checkHealth = async (): Promise<boolean> => {
  try {
    const response = await axios.get(`${API_BASE_URL}/health`, { timeout: 5000 });
    return response.status === 200;
  } catch {
    return false;
  }
};
