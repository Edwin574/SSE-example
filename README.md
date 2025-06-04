# Server-Sent Events (SSE) Simulation

A simple Django-based project that demonstrates the implementation and usage of Server-Sent Events (SSE) for real-time data streaming from server to client.

## Overview

This project provides a practical implementation of Server-Sent Events, a technology that allows servers to push updates to web clients over HTTP. Unlike WebSockets, SSE is unidirectional (server to client only) and is built on top of standard HTTP, making it simpler to implement and use in many scenarios.

## Features

- Real-time data streaming from server to client
- Django backend with Channels support
- Simple and clean implementation
- Easy to understand and extend
- Built-in simulation capabilities

## Technology Stack

- **Backend:**
  - Django 5.2.1
  - Django Channels 4.1.0
  - Django REST Framework 3.14.0
  - Daphne 4.2.0 (ASGI server)

- **Frontend:**
  - HTML5
  - JavaScript (Native EventSource API)
  - CSS

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/sse.git
   cd sse
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

## Running the Project

1. Start the development server:
   ```bash
   python manage.py runserver
   ```

2. Access the application at `http://localhost:8000`

## Usage

The project includes a simple simulation that demonstrates SSE in action. The server will send periodic updates to connected clients, which can be viewed in real-time in the browser.

## Project Structure

```
sse/
├── manage.py
├── requirements.txt
├── sse/          # Main Django project directory
└── sim/          # Simulation app directory
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Django Channels for providing the ASGI implementation
- The Django community for the excellent documentation and support 