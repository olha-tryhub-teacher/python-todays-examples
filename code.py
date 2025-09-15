@app.get("/home", response_class=HTMLResponse)
def ui_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/home/authors", response_class=HTMLResponse)
def ui_authors(request: Request, db: Session = Depends(get_db)):
    authors = crud.get_authors(db)
    return templates.TemplateResponse( #один рядок
        "authors.html", {"request": request, "authors": authors})





@app.get("/home/books", response_class=HTMLResponse)
def ui_books(request: Request, db: Session = Depends(get_db)):
    books = crud.get_books(db)
    return templates.TemplateResponse("books.html", {"request": request, "books": books})


@app.get("/home/authors/{author_id}",  response_class=HTMLResponse)
def ui_single_author(author_id: int, request: Request, db: Session = Depends(get_db)):
    db_author = crud.get_author(db, author_id=author_id)
    if not db_author:
        raise HTTPException(status_code=404, detail="Автор не знайдений")
    # отримуємо книжки саме цього автора
    books = db_author.books
    return templates.TemplateResponse(
        "author.html",
        {
            "request": request,
            "author": db_author,
            "books": books
        }
    )
