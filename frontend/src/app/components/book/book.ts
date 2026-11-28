import { CommonModule } from '@angular/common';
import { Component, signal } from '@angular/core';
import { ActivatedRoute, Router, RouterModule } from '@angular/router';
import { WebService } from '../../services/web-service';

@Component({
  imports: [CommonModule, RouterModule],
  selector: 'app-book',
  styleUrl: './book.scss',
  templateUrl: './book.html',
})
export class Book {

  book_info = signal<any>([]);

  constructor(
    private route: ActivatedRoute,
    private webService: WebService,
  ) {}

  ngOnInit() {
    const bookId = this.route.snapshot.paramMap.get('id');
    console.log('Book ID: ', bookId);

    this.loadBookInfo(bookId!);
  }

  loadBookInfo(bookId: string) {
    // Implementation for loading book information
    this.webService.getOneBook(bookId).subscribe((response: any) => {
      this.book_info.set(response);
      console.log('Book Info: ', this.book_info());
    });
  }
}
