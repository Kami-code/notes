package com.itheima.springcloud.controller;
import com.netflix.discovery.converters.Auto;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

@RestController
public class UserController {
    @Autowired
    private RestTemplate restTemplate;
    /**
     * 查找与用户相关的订单
     */
    @GetMapping("/findOrdersByUser/{id}")
    public String findOrderByUser(@PathVariable String id) {
        // 假设用户只有一个订单，并且订单id为123
        return this.restTemplate.getForObject("http://microservice-eureka-order/order/" + id, String.class);
    }
}
