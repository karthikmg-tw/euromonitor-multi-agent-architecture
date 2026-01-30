# Story 1.1: User Registration with Email/Password

Status: ready-for-dev

<!-- Note: Validation is optional. Run validate-create-story for quality check before dev-story. -->

## Story

As a new user,
I want to register an account with my email and password,
So that I can access the Passport AI Intelligence Assistant.

## Acceptance Criteria

### AC1: Successful Registration Flow
**Given:** I am on the registration page
**When:** I submit a valid email address and password (min 8 characters)
**Then:**
- A new user account is created in the PostgreSQL database
- My password is hashed using bcrypt before storage
- I receive a success message confirming registration
- I am redirected to the login page

### AC2: Duplicate Email Prevention
**Given:** I attempt to register with an already-used email
**When:** I submit the registration form
**Then:**
- I receive an error message "Email already registered"
- No duplicate account is created

### AC3: Validation Error Handling
**Given:** I submit an invalid email format or weak password (<8 chars)
**When:** I submit the registration form
**Then:**
- I receive specific validation error messages
- The form highlights the invalid fields

## Tasks / Subtasks

### Backend Implementation

- [ ] **Task 1: Create PostgreSQL Users Table** (AC: #1)
  - [ ] Create migration for `users` table with schema:
    - `id` UUID PRIMARY KEY (use `gen_random_uuid()`)
    - `email` VARCHAR(255) UNIQUE NOT NULL
    - `password_hash` VARCHAR(255) NOT NULL
    - `role` VARCHAR(50) DEFAULT 'user'
    - `subscription_tier` VARCHAR(50) NULL
    - `created_at` TIMESTAMP DEFAULT NOW()
    - `updated_at` TIMESTAMP DEFAULT NOW()
  - [ ] Add unique index on email (lowercase)
  - [ ] Add database triggers for `updated_at` timestamp

- [ ] **Task 2: Implement Password Hashing Service** (AC: #1)
  - [ ] Install `passlib[bcrypt]` or `pwdlib` (see tech research notes)
  - [ ] Create `PasswordService` class with:
    - `hash_password(plain_password: str) -> str` method using bcrypt cost factor 12
    - `verify_password(plain_password: str, hashed: str) -> bool` method
  - [ ] Write unit tests for password hashing and verification

- [ ] **Task 3: Create User Model and Repository** (AC: #1, #2)
  - [ ] Create SQLAlchemy `User` model mapping to `users` table
  - [ ] Create `UserRepository` with methods:
    - `create_user(email: str, password_hash: str) -> User`
    - `get_user_by_email(email: str) -> User | None`
  - [ ] Implement duplicate email check in repository

- [ ] **Task 4: Create Registration API Endpoint** (AC: #1, #2, #3)
  - [ ] Create Pydantic schemas:
    - `RegisterRequest(email: EmailStr, password: str)` with validation
    - `RegisterResponse(success: bool, message: str, redirect_url: str)`
  - [ ] Implement `POST /api/v1/auth/register` endpoint with:
    - Email format validation (Pydantic EmailStr)
    - Password length validation (min 8 characters)
    - Duplicate email check
    - Password hashing
    - User creation
    - Rate limiting (10 requests/minute per IP)
  - [ ] Add proper error handling and HTTP status codes:
    - 201 Created for success
    - 400 Bad Request for validation errors
    - 409 Conflict for duplicate email
  - [ ] Write integration tests for all scenarios

### Frontend Implementation

- [ ] **Task 5: Create Registration Form Component** (AC: #1, #3)
  - [ ] Install dependencies: `react-hook-form`, `zod`, `@hookform/resolvers`
  - [ ] Create Zod validation schema:
    - Email: `z.string().email("Please enter a valid email address")`
    - Password: `z.string().min(8, "Password must be at least 8 characters")`
  - [ ] Create `RegistrationForm` component using React Hook Form + zodResolver
  - [ ] Implement form fields:
    - Email input with real-time validation (on blur)
    - Password input with validation (as user types)
  - [ ] Add submit button with loading state
  - [ ] Implement form submission handler

- [ ] **Task 6: Create Registration Page** (AC: #1, #2, #3)
  - [ ] Create `/register` route
  - [ ] Build registration page layout with:
    - Page title: "Create an account to access market intelligence"
    - Registration form
    - "Already have an account? Login" link
  - [ ] Implement success handling:
    - Show success message
    - Redirect to `/login` after 2 seconds
  - [ ] Implement error handling:
    - Display field-specific validation errors inline
    - Display API errors (duplicate email, server error) as alert
  - [ ] Apply UX design tokens (colors, typography, spacing from UX spec)

- [ ] **Task 7: API Integration** (AC: #1, #2, #3)
  - [ ] Create API client method `registerUser(email, password)`
  - [ ] Implement error parsing from backend responses
  - [ ] Add loading states during API call
  - [ ] Disable form during submission to prevent double-submit

### Testing & Validation

- [ ] **Task 8: End-to-End Testing** (AC: #1, #2, #3)
  - [ ] Write E2E test: Successful registration flow
  - [ ] Write E2E test: Duplicate email prevention
  - [ ] Write E2E test: Email validation
  - [ ] Write E2E test: Password validation
  - [ ] Verify redirect to login page after success

- [ ] **Task 9: Security Validation** (AC: #1)
  - [ ] Verify password is hashed (never stored plain text)
  - [ ] Verify bcrypt cost factor is 12
  - [ ] Test rate limiting on registration endpoint
  - [ ] Verify CORS configuration allows only frontend origin
  - [ ] Test SQL injection prevention (parameterized queries)

## Dev Notes

### Critical Implementation Requirements

**🔥 SECURITY IMPERATIVES:**
- NEVER store passwords in plain text - always hash with bcrypt cost factor 12
- Use parameterized queries (SQLAlchemy ORM) to prevent SQL injection
- Normalize email to lowercase before storage/lookup
- Implement rate limiting: 10 requests/minute per IP on auth endpoints
- Enable CORS only for frontend origin (not wildcard)

**🏗️ Architecture Compliance:**
- This story establishes foundation for Epic 1 (Secure User Authentication & Access Control)
- Creates `users` table that will be used by Stories 1.2-1.8
- Default role is 'user' - Story 1.3 will add role assignment functionality
- `subscription_tier` field is nullable - Story 1.4 will populate it

**📦 Technology Stack (from Architecture):**
- **Backend:** FastAPI + SQLAlchemy + PostgreSQL
- **Password Hashing:** passlib[bcrypt] with cost factor 12 OR pwdlib with Argon2id (see tech research)
- **Frontend:** React + Vite + TailwindCSS + shadcn/ui
- **Validation:** Pydantic (backend), Zod + React Hook Form (frontend)

### Project Structure Notes

**Backend File Structure:**
```
app/
├── models/
│   └── user.py              # SQLAlchemy User model
├── schemas/
│   └── auth.py              # Pydantic RegisterRequest/Response
├── repositories/
│   └── user_repository.py   # User data access layer
├── services/
│   └── password_service.py  # Password hashing/verification
├── api/
│   └── auth.py              # Registration endpoint
└── migrations/
    └── versions/
        └── xxx_create_users_table.py
```

**Frontend File Structure:**
```
src/
├── pages/
│   └── RegistrationPage.tsx
├── components/
│   └── auth/
│       └── RegistrationForm.tsx
├── api/
│   └── auth.ts              # API client methods
├── schemas/
│   └── registration.ts      # Zod validation schemas
└── types/
    └── auth.ts              # TypeScript types
```

### Database Schema Details

**Users Table (PostgreSQL):**
```sql
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  role VARCHAR(50) DEFAULT 'user',
  subscription_tier VARCHAR(50),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_users_email ON users(LOWER(email));
```

**Why UUID over SERIAL?**
- Better for distributed systems (future scalability)
- Secure enough for user-facing URLs (Story 8.1+)
- Consider UUIDv7 if available (time-ordered for better index performance)
- Source: [pganalyze UUID vs Serial](https://pganalyze.com/blog/5mins-postgres-uuid-vs-serial-primary-keys)

### Latest Technical Research (January 2026)

**🚨 IMPORTANT: FastAPI Password Hashing Update**

Recent research shows FastAPI documentation has updated from `passlib` to `pwdlib`:
- **passlib is no longer maintained** (as of 2024-2025)
- **Official FastAPI recommendation:** Use `pwdlib` with Argon2id hashing
- **Legacy option:** passlib with bcrypt still works but consider migration

**Implementation Options:**

**Option A: Modern (pwdlib + Argon2id) - RECOMMENDED**
```python
from pwdlib import PasswordHash

password_hash = PasswordHash((
    ("argon2", {
        "memory_cost": 65536,
        "time_cost": 3,
        "parallelism": 4
    }),
))

# Hash password
hashed = password_hash.hash("password123")

# Verify password
is_valid = password_hash.verify("password123", hashed)
```

**Option B: Legacy (passlib + bcrypt) - STILL VALID**
```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto", bcrypt__rounds=12)

# Hash password
hashed = pwd_context.hash("password123")

# Verify password
is_valid = pwd_context.verify("password123", hashed)
```

**Decision:** Architecture specifies bcrypt, but pwdlib+Argon2id is more modern. Recommend using pwdlib unless there's a specific reason for bcrypt compatibility.

**Sources:**
- [FastAPI JWT Authentication Guide](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)
- [FastAPI passlib Discussion](https://github.com/fastapi/fastapi/discussions/11773)
- [Better Stack FastAPI Authentication](https://betterstack.com/community/guides/scaling-python/authentication-fastapi/)

**React Hook Form + Zod Integration:**

Latest pattern for 2026 (confirmed from multiple sources):
```typescript
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";

// Validation schema
const registerSchema = z.object({
  email: z.string().email("Please enter a valid email address"),
  password: z.string().min(8, "Password must be at least 8 characters")
});

type RegisterForm = z.infer<typeof registerSchema>;

// In component
const { register, handleSubmit, formState: { errors } } = useForm<RegisterForm>({
  resolver: zodResolver(registerSchema)
});
```

**Sources:**
- [FreeCodeCamp Zod + RHF Guide](https://www.freecodecamp.org/news/react-form-validation-zod-react-hook-form/)
- [Contentful RHF Validation](https://www.contentful.com/blog/react-hook-form-validation-zod/)
- [Abstract API Next.js 15 Type-Safe Forms](https://www.abstractapi.com/guides/email-validation/type-safe-form-validation-in-next-js-15-with-zod-and-react-hook-form)

### UX Design Compliance

**From UX Specification (ux-design-specification.md):**

**Design Principles:**
1. "ChatGPT Simplicity" - Single, intuitive interface
2. "Professional Delight" - Clean, business-appropriate aesthetic
3. "Confidence Through Simplicity" - Simple forms reduce anxiety

**Color Tokens:**
- Primary Blue (#2563EB): Submit button, active states, links
- Gray-900 (#111827): Form labels and text
- Red-500 (#EF4444): Error messages and invalid field borders
- Green-500 (#10B981): Success messages
- Gray-700: Label text

**Typography:**
- Form Labels: 14px, Semibold (600), Gray-700
- Input Text: 16px, Regular (400), Gray-900
- Error Messages: 14px, Regular (400), Red-500

**Spacing:**
- Form padding: 24px
- Field spacing: 16px between fields
- Button height: 40px (touch-friendly)

**Button Styling:**
- Primary "Register": Solid fill #2563EB, hover #1E40AF
- Disabled state: Gray with reduced opacity

**Error Messages (Specific Copy):**
| Scenario | Message |
|----------|---------|
| Duplicate email | "Email already registered. Please log in or use a different email." |
| Invalid email | "Please enter a valid email address." |
| Weak password | "Password must be at least 8 characters." |
| Network error | "Unable to create account. Please check your connection and try again." |

**Accessibility (WCAG AA):**
- All fields must have `<label>` elements
- Error messages associated via ARIA attributes
- Visible focus indicators
- Keyboard navigation support (Tab, Enter)
- 40px minimum touch targets

### Dependencies and Integration Points

**Story 1.1 Depends On:**
- **Story 2.1:** Project initialization (Vite + React + Tailwind + shadcn/ui must exist)
- **Infrastructure:** PostgreSQL database provisioned and accessible

**Stories That Depend on Story 1.1 (BLOCKING):**
- **Story 1.2:** User Login (requires user record to exist)
- **Story 1.3:** Role Assignment (requires users table with role field)
- **Story 1.4:** Subscription Tier Mapping (requires users table with subscription_tier field)
- **Story 1.5-1.8:** Permission enforcement (all require authenticated users)

**Integration Points:**
- Frontend connects to backend at `POST /api/v1/auth/register`
- Backend creates user in PostgreSQL `users` table
- Success response triggers frontend redirect to `/login`

### Testing Strategy

**Unit Tests:**
- Password hashing service (hash/verify methods)
- Email validation logic
- User repository methods

**Integration Tests:**
- Registration endpoint success scenario
- Duplicate email detection
- Validation error responses
- Database persistence verification

**E2E Tests (Playwright/Cypress):**
- Complete registration flow (fill form → submit → redirect)
- Error handling (duplicate email, validation errors)
- Accessibility compliance

**Security Tests:**
- Verify password is hashed (not plain text in DB)
- SQL injection prevention
- Rate limiting enforcement
- CORS policy validation

### Non-Functional Requirements

From Architecture Specification:

- **NFR8 (Data at Rest Encryption):** PostgreSQL encrypted via AWS RDS, passwords hashed with bcrypt
- **NFR9 (Data in Transit Encryption):** All API calls via TLS 1.3+, HTTPS enforced
- **NFR12 (Injection Prevention):** SQLAlchemy ORM with parameterized queries
- **NFR13 (Rate Limiting):** 10 requests/minute per IP on registration endpoint
- **NFR15 (Security Headers):** CORS restricted to frontend origin, security headers configured

### Business Context

**Epic 1 Objective:** Secure User Authentication & Access Control

**MVP Phase 1-2 (Months 1-4):**
- Email/password authentication with JWT tokens (NOT SSO yet)
- SSO integration deferred to Phase 5+

**User Archetypes Benefiting:**
1. **Sarah Chen (Market Analyst):** Needs seamless registration for audit/compliance
2. **Miguel Rodriguez (Category Manager):** Non-expert requiring simple, clear process
3. **Dr. Priya Kapoor (Senior Analyst):** Admin role assigned in Story 1.3

**Success Criteria:**
- User can register account in <30 seconds
- Zero plain-text passwords in database
- Audit trail captures registration events (user_id, timestamp, email)

### References

- [Source: epics.md → Epic 1 → Story 1.1]
- [Source: architecture.md → Authentication Strategy → JWT Tokens for MVP]
- [Source: architecture.md → Database Schema → Users Table]
- [Source: architecture.md → Non-Functional Requirements → NFR8-NFR15]
- [Source: ux-design-specification.md → Design System Foundation → Colors, Typography, Spacing]
- [Source: ux-design-specification.md → Authentication → Email/Password for MVP]
- [Source: prd.md → Product Scope → MVP Phase 1-2]
- [Source: prd.md → User Journeys → Sarah Chen, Miguel Rodriguez, Dr. Priya Kapoor]

## Dev Agent Record

### Agent Model Used

_To be filled by Dev Agent during implementation_

### Debug Log References

_To be filled by Dev Agent during implementation_

### Completion Notes List

_To be filled by Dev Agent during implementation_

### File List

_To be filled by Dev Agent during implementation_
