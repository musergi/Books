import { Component, OnInit } from '@angular/core';
import { Author } from '../author';
import { AuthorService } from '../author.service';

@Component({
  selector: 'app-authors',
  templateUrl: './authors.component.html',
  styleUrls: ['./authors.component.css']
})
export class AuthorsComponent implements OnInit {

  authors: Author[] = [];
  isAdding: boolean = false;

  constructor(private authorService: AuthorService) { }

  ngOnInit(): void {
    this.authorService.getAuthors().subscribe(authors => this.authors = authors);
  }

  get_long_name(author: Author): string {
    if (author.pseudonym)
      return author.pseudonym;
    return author.names.join(' ') + ' ' + author.surnames.join(' ');
  }

  toggleAdding() {
    this.isAdding = !this.isAdding;
  }
}
