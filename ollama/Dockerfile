# Use the official Ollama image as the base
FROM ollama/ollama

# Expose the necessary port
EXPOSE 11434

# Use a volume for persistence
VOLUME ["/root/.ollama"]

# Start the Ollama server in the background and wait for it to be ready
RUN systemctl start ollama && ollama wait

# Pull a model during build time
RUN ollama pull phi3:mini

# Start the Ollama server
CMD ["ollama", "serve", "--port", "11434"]