# Accessibility Best Practices

This will be a lot of list items until I figure out the layout for the file. Right now this is "rough".

- Wrap emojis in a `<span>` with an `aria-hidden="true"` attribute. This hides the emoji from screen readers while keeping it visible for your sighted users
  - Example: `<span aria-hidden="true">🗃️</span>`
- Have alt descriptions for all your images
- Make sure all your links have descriptive link text
- Use proper heading structure
- section spacing: according to Gemini, adding `<hr>` elements is the best practices way to add spacing betweeen h2 sections, but using `<br>` elements is just as good IMO and looks better. However, you should add them inside a span element for accessibility reasons:
  - `<span aria-hidden="true"><br></span>`
