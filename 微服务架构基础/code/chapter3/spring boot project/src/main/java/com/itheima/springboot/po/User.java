package com.itheima.springboot.po;

import java.io.Serializable;

public class User implements Serializable {
    private static final long serialVersionUID = 1L;
    private Integer id;
    private String username;
    private String address;
    public Integer getId() {
        return id;
    }
    public String getAddress() {
        return address;
    }
    public String getUsername() {
        return username;
    }
    public void setAddress(String address) {
        this.address = address;
    }
    public void setId(Integer id) {
        this.id = id;
    }
    public void setUsername(String username) {
        this.username = username;
    }
}
