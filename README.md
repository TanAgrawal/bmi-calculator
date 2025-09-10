## BMI Calculator

This is a simple BMI (Body Mass Index) Calculator built using Streamlit.

### Features
- Input height (cm,m,feet) and weight (kg)
- Calculates BMI instantly
- Displays BMI category (Extremely Underweight,Underweight, Healthy, Overweight, Extremely Overweight)

### Installation & Usage
#### 1. Clone the Repository
```bash
git clone https://github.com/TanAgrawal/bmi-calculator.git
cd bmi-calculator
```

#### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 3. Run the App
```bash
streamlit run BMI_Calculator.py
```

### Deployment on Streamlit Cloud
1. Push this project to a GitHub repository.
2. Go to [Streamlit Cloud](https://share.streamlit.io/) and log in.
3. Click New App, select the repository, and deploy.

### Project Structure
```
📂 bmi-calculator
│-- BMI_Calculator.py   # Main Streamlit app
│-- requirements.txt    # Dependencies
│-- README.md           # Project Documentation
```

### Dependencies (requirements.txt)
```
streamlit

```

### License
This project is open-source and free to use.


````markdown
# WhatsApp Chatbot — Final Integrated Architecture (Editable MD Version with Diagram)

This file explains the **complete end-to-end architecture** for a WhatsApp chatbot that can handle multiple queries from multiple users, provide context/intent-based answers, and maintain memory of past conversations. You can edit this file freely.

---

## 🔄 End-to-End Working Flow (Step by Step)

### 1. **User Sends Message**
- **Flow:** User → WhatsApp App → **WhatsApp Business Platform (WABA)**.
- **Example:** *“What are the visiting hours for Apollo Hospital?”*

### 2. **Webhook Receiver**
- **Tech:** Flask (or FastAPI).
- **Role:** Validates incoming WhatsApp webhook, extracts message details.
- **Action:** Immediately pushes the message to the **Message Queue**.

### 3. **Message Queue**
- **Tech:** Kafka (high scale) or AWS SQS (managed).
- **Role:** Buffers messages to prevent overload, ensures no message is lost.
- **Action:** Message is now safe in the queue and ready for processing.

### 4. **Router Service**
- **Role:** Decides where the message should go.
- **Logic:**
  - Identify tenant (banking, healthcare, retail, etc.).
  - Send message to **NLP Service** for intent detection.

### 5. **NLP / Intent Detection**
- **Tech:** Gemini/OpenAI (complex queries), Rasa/Dialogflow (fast intent classification).
- **Role:** Understands what the user wants.
- **Examples:**
  - Input: *“Book a doctor’s appointment.”* → Intent: `book_appointment`.
  - Input: *“Apollo Hospital timings”* → Intent: `hospital_info`.

### 6. **Dialog Manager (Context + Memory)**
- **Tech:** Redis (short-term memory), PostgreSQL (long-term memory).
- **Role:** Keeps track of conversation history.
- **Examples:**
  - User: *“Book appointment”* → remembers user asked about Apollo.
  - Next User message: *“Tomorrow at 10 AM”* → links back to appointment booking context.

### 7. **Domain Microservices**
- **Role:** Executes actual tasks.
- **Examples:**
  - **Scraper Microservice** → Searches hospital/website info.
  - **OCR Microservice** → Extracts text from documents/images.
  - **Order Service** → Tracks delivery status.

### 8. **Knowledge Base + Pinecone**
- **Tech:** Pinecone (vector DB).
- **Role:** Retrieves relevant documents/FAQs for RAG.
- **Example:** Query: *“Apollo Hospital timings”* → retrieves info from Pinecone embeddings.

### 9. **LLM Answer Generation**
- **Tech:** Gemini/OpenAI.
- **Role:** Combines retrieved context + conversation memory to generate a natural reply.
- **Example:**
  - Pinecone returns: “Apollo Hospital visiting hours are 10 AM – 6 PM.”
  - LLM responds: *“Apollo Hospital is open for visitors between 10 AM and 6 PM daily. Would you like me to also check doctor availability?”*

### 10. **Outgoing Queue**
- **Tech:** Kafka/RabbitMQ.
- **Role:** Holds generated responses before sending.
- **Benefit:** Prevents API throttling and ensures retries if WhatsApp fails.

### 11. **WhatsApp Sender Service**
- **Tech:** Worker with token-bucket rate limiter (Redis).
- **Role:** Sends replies via WhatsApp Business API at safe speeds.
- **Example:** Outbox → WhatsApp API → User sees reply instantly.

---

## 🧠 Memory (Per User)
- **Short-Term (Redis):** Tracks current conversation session (intent, last few messages).
- **Long-Term (PostgreSQL):** Stores full conversation history for personalization and analytics.
- **Benefit:** Every conversation feels continuous, not like starting fresh.
- **Example:**
  - User: *“Track my last order.”*
  - Bot (via PostgreSQL history): *“Sure, your last order was #1234, delivered yesterday.”*

---

## 📊 Scalable, Multi-User Handling
- **Queues + Worker Pools:** Allow thousands of messages processed in parallel.
- **Kubernetes Deployment:** Each microservice (NLP, Router, Scraper, OCR, Knowledge) scales independently.
- **Caching:** Redis caches popular answers to respond instantly.
- **Result:** Millions of users can chat simultaneously without slowing down.

---

## 🎯 Example Full Flow
1. User: *“Book a doctor at Apollo tomorrow.”*
2. WhatsApp → WABA → Flask Webhook → Queue.
3. Router → NLP: Intent = `book_appointment`.
4. Dialog Manager: remembers “Apollo” from past message.
5. Scraper Microservice: finds available slots.
6. Pinecone: retrieves hospital info.
7. Gemini/OpenAI: builds natural response.
8. Response → Outgoing Queue → WhatsApp Sender → User.
9. User sees: *“Your appointment at Apollo Hospital is confirmed for tomorrow at 10 AM.”*

---

## 🖼️ Architecture Diagram (Mermaid)
You can view this diagram in **VS Code Markdown Preview Enhanced** or GitHub preview.

```mermaid
graph TD
  A[User WhatsApp App] -->|Message| B[WhatsApp Business Platform]
  B --> C[Webhook Receiver (Flask/FastAPI)]
  C --> D[Incoming Queue (Kafka/SQS)]
  D --> E[Router Service]
  E --> F[NLP Service (Gemini/Rasa/Dialogflow)]
  F --> G[Dialog Manager (Redis/PostgreSQL)]
  G --> H{Route Decision}
  H --> I[Domain Microservices]
  H --> J[Knowledge Base (Pinecone)]
  J --> K[LLM (Gemini/OpenAI)]
  I --> L[Outgoing Queue]
  K --> L[Outgoing Queue]
  L --> M[WhatsApp Sender Service]
  M --> B
  B -->|Reply| A
````

---

## ✅ Final Notes

* **Reliable:** Queues ensure no dropped messages.
* **Smart:** NLP + LLM + Pinecone give intelligent, context-aware answers.
* **Memory-Driven:** Redis + PostgreSQL make chats continuous.
* **Scalable:** Kubernetes + Kafka handle millions of users.
* **Extensible:** Easy to plug in more microservices (payments, ticketing, retail).

👉 This is your **complete, production-grade working flow** in an editable Markdown file, now with a Mermaid diagram you can preview in VS Code.

```
```
