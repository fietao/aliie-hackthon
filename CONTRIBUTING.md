# Contributing to GrocerySort

Thank you for your interest in contributing to GrocerySort! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Follow best practices
- Test your changes before submitting

## Getting Started

### 1. Fork the Repository
```bash
git clone https://github.com/yourusername/aliie-hackthon.git
cd aliie-hackthon
```

### 2. Create a Branch
```bash
git checkout -b feature/your-feature-name
```

### 3. Set Up Development Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Development Guidelines

### Code Style

- **Python:** Follow PEP 8
  ```bash
  pip install flake8
  flake8 app.py ai.py
  ```

- **JavaScript:** Use standard conventions
  - Use `const` and `let` (not `var`)
  - Use camelCase for variables
  - Use UPPER_CASE for constants

- **CSS:** Use BEM naming convention
  ```css
  .block { }
  .block__element { }
  .block--modifier { }
  ```

### Comments & Documentation

- Write clear comments for complex logic
- Use docstrings for Python functions
- Update README if adding features

Example Python docstring:
```python
def categorize(item):
    """
    Categorize a grocery item.
    
    Args:
        item (str): Item name to categorize
        
    Returns:
        str: Category name
    """
    pass
```

### Testing

- Test your changes locally before submitting
- Test on different browsers (Chrome, Firefox, Safari)
- Test on mobile devices

### Commit Messages

Follow conventional commits format:

```
type(scope): subject

body

footer
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Code style
- `refactor`: Code refactoring
- `test`: Tests
- `chore`: Maintenance

Examples:
```bash
git commit -m "feat(categorization): add seafood category"
git commit -m "fix(ui): correct button alignment on mobile"
git commit -m "docs: update deployment guide"
```

## Making Changes

### Adding a New Category

1. **Update `ai.py`**
   ```python
   category_keywords = {
       "new category": ["keyword1", "keyword2", ...]
   }
   ```

2. **Update `result.js`**
   ```javascript
   const categoryIcons = {
       "new category": "emoji"
   }
   ```

3. **Update styles** if needed in `style.css`

### Fixing Bugs

1. Identify the issue
2. Create a branch: `git checkout -b fix/bug-name`
3. Make changes
4. Test thoroughly
5. Submit pull request

### Improving Performance

- Profile code before optimizing
- Measure performance impact
- Document performance improvements

## Submitting Changes

### Pull Request Process

1. **Update your branch**
   ```bash
   git fetch origin
   git rebase origin/main
   ```

2. **Push changes**
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create Pull Request**
   - Title: Clear, concise description
   - Description: Explain changes and why
   - Link related issues: `Closes #123`

4. **PR Checklist**
   - [ ] Changes are tested
   - [ ] Documentation updated
   - [ ] No breaking changes
   - [ ] Code follows style guide
   - [ ] Commit messages are clear

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
Describe how you tested changes

## Screenshots (if UI changes)
Include screenshots of changes

## Related Issues
Closes #123
```

## Review Process

- Code review by maintainers
- Address feedback and suggestions
- Re-request review after changes
- Merge once approved

## Documentation

### README Updates
- Explain new features clearly
- Include examples
- Update version history

### Code Comments
- Explain "why", not "what"
- Use clear language
- Keep comments up-to-date

## Reporting Issues

### Bug Report
```markdown
## Description
Clear description of the bug

## Steps to Reproduce
1. ...
2. ...
3. ...

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- Browser: Chrome 120
- OS: Windows 11
- Python: 3.11
```

### Feature Request
```markdown
## Feature Description
Clear description of requested feature

## Use Case
Why is this feature needed?

## Proposed Solution
How should this work?

## Alternatives
Other possible approaches
```

## Project Structure

```
aliie-hackthon/
├── app.py              # Flask app
├── ai.py               # Categorization logic
├── config.py           # Configuration
├── requirements.txt    # Dependencies
├── html/               # HTML templates
├── static/             # CSS, JS, images
└── docs/               # Documentation
```

## Helpful Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [MDN Web Docs](https://developer.mozilla.org/)
- [PEP 8 Style Guide](https://pep8.org/)
- [Git Documentation](https://git-scm.com/doc)

## Questions?

- Check existing issues and discussions
- Create a new discussion
- Contact maintainers

## License

By contributing, you agree your changes are licensed under the MIT License.

---

Thank you for contributing to GrocerySort! 🎉
