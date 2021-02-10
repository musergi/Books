import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Author } from './author';

@Injectable({
  providedIn: 'root'
})
export class AuthorService {
  adrress: string = 'http://0.0.0.0:8000/api'

  constructor(private http: HttpClient) { }

  getAuthors(offset: number=0, count: number=0) : Observable<Author[]> {
    return this.http.get<Author[]>(this.adrress + '/authors/')
  }
}
