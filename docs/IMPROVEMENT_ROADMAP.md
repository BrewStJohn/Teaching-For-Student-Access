# Teaching collection improvement roadmap

Recorded October 21, 2026, from the workspace review on October 18, 2026.

This roadmap covers the student-facing `Teaching` repository and the sibling
`Teaching Resources` folder used for reusable examples and older camp materials.
The aim is to make lessons easier to find, run, teach, and maintain while keeping
each class project understandable and self-contained.

These are proposed improvements, not completed fixes. Examples below use paths
relative to the workspace containing both folders. `Teaching Resources` is outside
this Git repository, so changes there need a separate backup or versioning plan.

## Review baseline

The review inventoried the workspace, parsed all 288 Python files, checked the 83
distinct JavaScript files represented by 142 copies, scanned local HTML asset
references, and inspected representative lessons and applications. Virtual
environments, Git internals, caches, and build output were excluded.

- Nine Python files failed syntax checks. Some are intentional unfinished exercises.
- Eleven HTML references pointed to missing local stylesheets.
- Of 272 folders identified by common entry-point filenames, six had a README.
- Across 826 source files, there were 381 additional copies of identical nonempty
  files. Some duplication supports self-contained class handouts.
- The JavaScript syntax checks passed, but a targeted check reproduced a 2048
  movement lock.

These counts describe the October 18 snapshot. Every application was not run,
and every image or other asset was not visually inspected.

## 1. Remove credentials and improve authentication examples

**Priority: first.** Teaching examples should show habits students can safely reuse.

Observed examples:

- `Teaching/Sunday/L6/Flask DB Intro/main.py` and its Tuesday counterpart contain
  a hardcoded MySQL root credential.
- `Teaching/Tuesday/L6/Science_Lab/app.py` also contains a hardcoded root credential.
- `Teaching Resources/Old Camps/FlaskCamp2/Game App Final/main.py` stores passwords
  directly, compares them directly during login, and prints the session secret.
  The archived 2025 copy repeats these patterns.

Planned actions:

- [ ] Read credentials from environment variables and provide `.env.example` files
  containing placeholders or clearly labeled local classroom defaults.
- [ ] Use a database account restricted to the application's database.
- [ ] Replace direct password storage and comparison with password hashing and
  hash verification; document how existing demonstration accounts are reset.
- [ ] Remove secret logging and keep local `.env` files out of version control.
- [ ] Rotate any real credential that has been shared or committed.

Completion check: distributed examples contain no real credentials, authentication
examples store password hashes, and setup instructions explain configuration.

## 2. Make completed examples reliably runnable

**Priority: first.** Separate intentionally incomplete starters from reference
solutions so students can tell what should work immediately.

Observed examples:

- `Teaching Resources/L4/Py Map Adventure FINAL/main.py` has an unfinished
  `move_player` function whose comment-only body causes a syntax error. That folder
  also contains `final.py`, so the intended entry point needs to be explicit.
- `Teaching Resources/L5/MyMDB FINAL/index.html` and
  `Teaching Resources/L5/Battleship FINAL/index.html` reference `css/style.css`,
  while their stylesheets are alongside the HTML. Several class copies repeat this.
- `Teaching Resources/L5/Intro to Pygame FINAL/ball.py` loads
  `Intro to Pygame FINAL/ball.png`, which fails when launched from its own folder.
- In `Teaching Resources/L5/2048 FINAL/script.js`, pressing Up when tiles occupy
  only the top row locks further input. `shiftUp()` starts no animations, so no
  callback reaches `endOfTurn()` to reset the movement flag.

Planned actions:

- [ ] Label starter, exercise, demonstration, and solution files consistently and
  document which file to run. Keep deliberate gaps clearly marked.
- [ ] Fix syntax failures in files designated as runnable reference solutions.
- [ ] Repair the missing stylesheet references across affected copies.
- [ ] Resolve Python asset paths relative to the source file, using `pathlib`,
  rather than relying on the terminal's current directory.
- [ ] Fix 2048's zero-animation movement path and check all four directions.
- [ ] Run each completed project from its own folder using its documented command.

Completion check: reference solutions launch as documented with their assets,
and the reproduced 2048 scenario leaves input responsive.

## 3. Give lessons predictable documentation

**Priority: next.** The main README explains how to obtain and protect class files;
individual lessons need equally clear instructions for using them.

Use `Teaching/Sunday/L6/Flask WebSockets/README.md` as a practical starting example.
Keep lesson documentation short and suitable for the students taking that lesson.

Planned actions:

- [ ] Create a reusable lesson README template covering learning objectives,
  prerequisites, required runtime version, dependencies, and exact launch commands.
- [ ] Name the starter and solution entry points and describe the expected result.
- [ ] Include checkpoints, extension challenges, and common troubleshooting steps.
- [ ] Add dependency manifests where third-party packages are required, especially
  for Pygame, data analysis, scraping, Flask, and machine-learning projects.
- [ ] Add a lesson index mapping class folders to topics and canonical resources.
- [ ] Document current lessons first, then improve archives as they are reused.

Completion check: someone unfamiliar with a lesson can locate its entry point,
install its dependencies, run it, and understand the intended learning outcome.

## 4. Control duplication between class folders

**Priority: next.** Keep convenient class copies while reducing the number of places
that require manual fixes.

Planned actions:

- [ ] Choose a canonical source for each reusable lesson, preferably in
  `Teaching Resources`, and record its version or revision when distributing it.
- [ ] Add a small distribution script that copies selected lessons and required
  assets into day/class folders.
- [ ] Have the script preview changes and avoid overwriting class-specific work
  without an explicit choice.
- [ ] Record intentional classroom variations so they are distinguishable from drift.
- [ ] Keep archived snapshots clearly labeled and independently runnable.

Completion check: a fix can be made in one canonical lesson and deliberately
distributed to the relevant classes without losing local teaching changes.

## 5. Add lightweight verification

**Priority: alongside repairs.** Focus automation on failures that interrupt class
and on the behavior each lesson is intended to demonstrate.

Planned actions:

- [ ] Check Python and JavaScript syntax for designated runnable examples.
- [ ] Scan HTML for missing local scripts, stylesheets, and images.
- [ ] Track deliberate starter gaps explicitly so checks remain useful.
- [ ] Add focused behavior checks for game rules, movement boundaries, and form
  validation, including the 2048 input-lock regression.
- [ ] Run database integration tests against a dedicated test database.
- [ ] Add checks to the repository workflow after their scope is established.

The existing Science Lab `tests/test_mysql_crud.py` imports the configured app and
writes temporary records to its configured MySQL database. Separate that test
configuration from the classroom database and document setup and cleanup.

Completion check: a documented verification command catches known reference
failures, and database tests cannot accidentally use the normal classroom database.

## 6. Clarify repository hygiene and distribution rules

**Priority: ongoing.** Make it clear which files belong in student downloads and
which remain local instructor resources.

Planned actions:

- [ ] Remove tracked Python cache files from version control and ignore
  `__pycache__/` and `*.pyc` going forward.
- [ ] Ignore local virtual environments, build output, and machine-specific files.
- [ ] Review the existing `**/*FINAL/` exclusion in `Teaching/.gitignore` and
  document whether solutions should be distributed or kept instructor-only.
- [ ] Distinguish intentional sample databases from generated runtime databases;
  provide seed or reset instructions for reusable datasets.
- [ ] Document how canonical resources outside the student repository are backed up.
- [ ] Preserve existing local edits and classroom work during cleanup or redistribution.

Completion check: student downloads contain the intended materials, generated files
stay out of commits, and the solution-sharing policy is explicit.

## Suggested implementation order

1. Remove credentials and repair broken completed examples.
2. Create the lesson README template and document lessons currently being taught.
3. Introduce canonical lesson versions and controlled distribution.
4. Add focused verification and tidy repository rules incrementally.

Keep changes small enough to review and verify before the next class uses them.
