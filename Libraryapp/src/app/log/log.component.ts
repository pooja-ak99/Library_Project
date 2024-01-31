import { Component } from '@angular/core';
import { ApicallService } from '../apicall.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-log',
  templateUrl: './log.component.html',
  styleUrls: ['./log.component.css']
})
export class LogComponent {
  constructor(private logapi:ApicallService, private router:Router){}
  data1={
    'username':"",
    'password':"",
  }

  onsubmit(){
    console.log(this.data1)
    this.logapi.login(this.data1).subscribe((res)=>
    {
      console.log(res);
      localStorage.setItem('token',"token "+res.token);
      console.log(localStorage.getItem('token'));
      this.router.navigate([""])
    })
  }

}
