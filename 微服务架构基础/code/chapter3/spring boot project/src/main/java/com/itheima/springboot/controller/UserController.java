package com.itheima.springboot.controller;


import com.itheima.springboot.po.User;
import com.itheima.springboot.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@CrossOrigin(maxAge = 3600)
@RestController
public class UserController {
    //注入用户Service
    @Autowired
    private UserService userService;
    //查询所有用户
    @RequestMapping("/user/userList")
    public List<User> getAllUsers() {
        List<User> list = this.userService.getAllUsers();
        return list;
    }
    //删除用户
    @RequestMapping("/user/delete/{id}")
    public void delete(@PathVariable Integer id) {
        this.userService.deleteUser(id);
    }
}
