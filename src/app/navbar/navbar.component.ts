import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  org: string = "Organizations";
  eve: string = "Events";
  ema: string = "Email";
  


  constructor() { }

  ngOnInit(): void {
  }

}
