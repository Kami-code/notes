package com.itheima.springcloud.po;

public class Order {
    private String id;
    private Double price;
    private String receiverName;
    private String receiverAddress;
    private String receiverPhone;

    public void setId(String id) {
        this.id = id;
    }
    public void setPrice(Double price) {
        this.price = price;
    }
    public Double getPrice() {
        return price;
    }
    public String getId() {
        return id;
    }
    public String getReceiverAddress() {
        return receiverAddress;
    }
    public String getReceiverName() {
        return receiverName;
    }
    public String getReceiverPhone() {
        return receiverPhone;
    }
    public void setReceiverAddress(String receiverAddress) {
        this.receiverAddress = receiverAddress;
    }
    public void setReceiverName(String receiverName) {
        this.receiverName = receiverName;
    }
    public void setReceiverPhone(String receiverPhone) {
        this.receiverPhone = receiverPhone;
    }
    @Override
    public String toString() {
        return "Order [id=" + id + ", price=" + price + ", " + "receiverName=" + receiverName + ", receiverAddress="
                + receiverAddress + ", receiverPhone=" + receiverPhone + "]";
    }
}
