from fastapi import FastAPI, Form, HTTPException, Depends, Cookie
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel

app = FastAPI()

# Simulated user data (replace this with your user authentication logic)
users_db = [
    {"username": "user1", "password": "password1"},
    {"username": "user2", "password": "password2"},
]

class User(BaseModel):
    username: str
    password: str

@app.get("/", response_class=HTMLResponse)
async def login_page():
    return """
    <!DOCTYPE html>
    <html>
    <head>
      <link rel="stylesheet" type="text/css" href="login.css">
      <title>Login - To-Do List App</title>
    </head>
    <body>
      <div class="login-container">
        <h1>Login</h1>
        <form id="loginForm" action="/login" method="post">
          <input type="text" name="username" placeholder="Username" maxlength="40">
          <input type="password" name="password" placeholder="Password" maxlength="40">
          <button type="submit" id="loginButton">Log In</button>
        </form>
      </div>
    </body>
    </html>
    """

@app.post("/login")
async def login(user: User, response: HTMLResponse):
    # Check if the user exists (replace this with your user authentication logic)
    authenticated_user = next((u for u in users_db if u["username"] == user.username and u["password"] == user.password), None)
    
    if authenticated_user:
        # Generate a token (you can use a library like PyJWT)
        token = "your_generated_token_here"
        
        # Set the token as a cookie
        response.set_cookie(key="token", value=token, path="/")
        
        # Redirect to the protected page
        return RedirectResponse(url="/main")
    
    raise HTTPException(status_code=401, detail="Invalid credentials. Please try again.")

@app.get("/main")
async def main_page():
    # Add your protected page logic here
    return {"message": "Welcome to the main page!"}
