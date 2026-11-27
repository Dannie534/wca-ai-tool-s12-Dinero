# Dinero 💰 - AI-Powered Smart Chama Assistant

WeCan Academy - Season 12 - Group Project
ChamaWise Group
Members: Duncan, Oliver, Ian
Model: Claude Haiku 5.5

Dinero is a smart assistant for Kenyan chamas. It remembers your whole conversation, tracks members and payments, and gives you a clean end-of-session summary.

## How to run
1. pip install -r requirements.txt
2. Create .env with: ANTHROPIC_API_KEY=your_key_here
3. python dinero.py

## What Dinero Can Do
1. Chat with Memory - Talk to Dinero for 6 turns. It remembers every member and payment you mention.
2. Manage Chama - Add members, record payments, view balances. Saved in dinero_data.json.
3. Knowledge Base - Dinero reads chama rules from knowledge.txt every time it starts.
4. JSON + Retry - Dinero must reply in valid JSON. If it fails, Dinero retries once automatically.
5. Final Summary - When you type exit, Dinero makes one final AI call and saves a summary to sessions/session_YYYY-MM-DD_HH-MM.json.
6. Open Past Sessions - Re-open any old session from the menu.
7. Error Handling - Empty input, bad JSON, API fail, missing file = no crash.
8. Security - API key from .env only, never in code.
9. Prompts - 2x R-T-C-C-O prompts (system + summary).

## Sample Proof
See samples/sample_session.json for a full 6-turn conversation + summary.
Turn 6 proves memory: it remembered Turns 1, 2 and 4.
- Duncan: Paid 500, Owes 500
- Oliver: Paid 1000, Paid in full
- Ian: Paid 0, Owes 1000
- Total collected: 1500 KES