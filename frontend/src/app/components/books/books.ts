import { Component, signal } from '@angular/core';
import { WebService } from '../../services/web-service'; 
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  imports: [CommonModule, RouterModule],
  selector: 'app-books',
  providers: [],
  styleUrl: './books.scss',
  templateUrl: './books.html',
  standalone: true
})
export class Books {

  books_list = signal<any>([]);

  page: number = 1;

  constructor(private webService: WebService) {}

  ngOnInit(){
    this.loadBooks();
  }

  loadBooks() {
    this.webService.getBooks(this.page).subscribe((response: any) => {
      this.books_list.set(response);
      console.log('Book Info: ', this.books_list());
    });
  }

  goToBook(bookId: string){
    console.log('GOING TO BOOK: ', bookId);
  }

}
