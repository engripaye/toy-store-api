---

```markdown
# 🧸 Toy Store API (FastAPI + Python)

A beginner-friendly project built with **FastAPI** to explore the fundamentals of Python API development.  
The API simulates a simple **Toy Store** where you can **add, list, update, and delete toys** using in-memory storage (Python lists & dictionaries).

---

## 🚀 Project Goal
The main goal of this project is to **learn FastAPI basics** and core **Python API concepts** through hands-on practice.

---

## ✨ Features
- ➕ **Add Toys** – Create new toy entries.  
- 📋 **List Toys** – Retrieve all stored toys.  
- ✏️ **Update Toys** – Modify toy details.  
- ❌ **Delete Toys** – Remove toys from the collection.  

*(Note: Data is stored in memory only and resets when the server restarts.)*

---

## 🛠️ Skills Practiced
- ✅ FastAPI routes (`@app.get`, `@app.post`, `@app.put`, `@app.delete`)  
- ✅ Handling **JSON requests & responses**  
- ✅ Managing data with **Python lists & dictionaries**  
- ✅ Understanding **CRUD API patterns**  

---

## 📂 Project Structure
```

toystore-api/
│── main.py         # FastAPI application
│── requirements.txt # Project dependencies
└── README.md        # Project documentation

````

---

## ⚡ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/toystore-api.git
   cd toystore-api
````

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the FastAPI server**

   ```bash
   uvicorn main:app --reload
   ```

---

## 🌐 API Endpoints

| Method | Endpoint     | Description        |
| ------ | ------------ | ------------------ |
| GET    | `/toys`      | List all toys      |
| POST   | `/toys`      | Add a new toy      |
| PUT    | `/toys/{id}` | Update toy details |
| DELETE | `/toys/{id}` | Delete a toy       |

---

## 📖 Learning Notes

This project is part of my journey to **master FastAPI** and build a strong foundation in **Python backend development**.

Future extensions may include:

* 🗄️ Adding database persistence (SQLite/PostgreSQL)
* 🔒 Basic authentication & validation
* 📦 Dockerization for deployment

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is licensed under the **MIT License**.

---

```

---

Would you like me to also **add sample request/response JSON payloads** in the README (so others can test endpoints quickly with Postman or curl)?
```
