# an-func-util
Analysis North utilities utilizing the Func-to-Web framework.

Run with

    uv run main.py

To get a wider display area, I modified the style.css file in the 
func-to-web library code. Here is the section to modify:

    .form-page .container {
        background: var(--white);
        padding: 2rem;
        border-radius: 16px;
        box-shadow: var(--shadow-lg);
        width: 900px;
        animation: fadeIn 0.3s ease-out;
    }

The `width` property sets the size.
