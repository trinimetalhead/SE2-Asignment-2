# User Acceptance Tests (UAT)

## 1. Employer Functions

### Test Case: Create Internship Position
**Steps:**
1. Login as employer
2. Navigate to position creation
3. Enter position details:
   - Title: "Junior Developer"
   - Description: "Entry level position"
   - Requirements: "Python knowledge"
4. Submit position

**Success Criteria:**
- Position appears in employer's positions list
- Position is searchable by students
- All entered details are displayed correctly

### Test Case: Review Shortlisted Candidates
**Steps:**
1. Login as employer
2. View shortlisted candidates for a position
3. Accept/reject candidates

**Success Criteria:**
- Can view all shortlisted candidates
- Can successfully accept/reject candidates
- Status updates immediately

## 2. Staff Functions

### Test Case: Shortlist Students
**Steps:**
1. Login as staff
2. Select internship position
3. Search for eligible students
4. Add students to shortlist

**Success Criteria:**
- Students are successfully added to shortlist
- Shortlist is visible to employer
- Multiple students can be added

## 3. Student Functions

### Test Case: View Shortlisted Positions
**Steps:**
1. Login as student
2. View positions they're shortlisted for
3. Check status of applications

**Success Criteria:**
- Can see all positions they're shortlisted for
- Status (pending/accepted/rejected) is clearly displayed
- Can view position details