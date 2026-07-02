# Business Logic vs Presentation Logic

In software systems, the work performed when handling a user request is usually divided into two main categories:

---

## 1. Business Logic (What the system does)

Business logic refers to the **core rules and processing of data** inside an application. It defines how information is validated, transformed, and stored.

### Examples:
- Validating user input (e.g., email format, password rules)
- Checking if a user already exists in a database
- Hashing or encrypting sensitive data
- Saving or updating data in storage
- Applying application rules (e.g., “users must be unique”)

### Key idea:
> Business logic defines **what should happen** and **how decisions are made**.

---

## 2. Presentation Logic (What the user sees)

Presentation logic is responsible for **how results are shown to the user**. It focuses on formatting and delivering information in a readable way.

### Examples:
- Displaying success or error messages
- Showing formatted data on a web page or screen
- Redirecting the user to another page or view
- Structuring output (HTML, JSON, UI components)

### Key idea:
> Presentation logic defines **how information is presented to the user**.

---

## Simple Comparison

| Type | Purpose | Focus |
|------|--------|-------|
| Business Logic | Process and rules | Data + decisions |
| Presentation Logic | Output and display | User experience |

---

## Why this separation is important

Keeping these two parts separate helps to:

- Make code easier to understand
- Improve maintainability
- Allow reuse of business rules in different interfaces
- Make testing simpler and more reliable

---

## Simple Analogy

- **Business logic** = the brain (thinking and decision-making)
- **Presentation logic** = the face (communication and expression)

---

## Summary

- Business logic handles **processing and rules**
- Presentation logic handles **displaying results**
- Good software design keeps them clearly separated