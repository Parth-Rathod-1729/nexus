import { createContext, useContext } from 'react';

export const VideoContext = createContext(null);
export const LogoutContext = createContext(null);

export function useVideo() {
  return useContext(VideoContext);
}
