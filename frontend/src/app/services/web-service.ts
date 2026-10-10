import { Service, inject } from '@angular/core';

import { HttpClient } from '@angular/common/http';

@Service()
export class WebService {

    private http = inject(HttpClient);

    pageSize = 10;

    //Books Endpoints
    getBooks(page: number) {
        return this.http.get(`http://localhost:5000/api/v1.0/media/books`, {
            params: {
                page,
                limit:this.pageSize
            }
        });
    }

}
