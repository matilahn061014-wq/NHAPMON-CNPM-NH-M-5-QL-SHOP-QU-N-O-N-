products = [
    {"id": 101, "name": "Váy hoa nhí", "price": 250000},
    {"id": 102, "name": "Áo sơ mi lụa", "price": 180000},
    {"id": 103, "name": "Quần jean ống rộng", "price": 320000}
]

def delete_product_process(product_id, user_role):
    if user_role != "Admin":
        return "❌ THẤT BẠI: Bạn không có quyền xóa."

    product = None
    for p in products:
        if p["id"] == product_id:
            product = p
            break

    if product is None:
        return "❌ THẤT BẠI: Không tìm thấy sản phẩm."

    confirmation = input("Xác nhận xóa (y/n): ")
    if confirmation.lower() != "y":
        return "⚠️ Thao tác xóa đã bị hủy."

    products.remove(product)
    return f"✅ Đã xóa sản phẩm {product['name']}."

current_role = "Admin"

for p in products:
    print(p)

result = delete_product_process(102, current_role)
print(result)

for p in products:
    print(p)
const readline = require("readline");

// Dữ liệu mẫu
let products = [
    { id: 101, name: "Váy hoa nhí", price: 250000 },
    { id: 102, name: "Áo sơ mi lụa", price: 180000 },
    { id: 103, name: "Quần jean ống rộng", price: 320000 }
];

// Hàm xóa sản phẩm
function deleteProductProcess(productId, userRole) {
    if (userRole !== "Admin") {
        console.log("❌ THẤT BẠI: Bạn không có quyền xóa.");
        return;
    }

    const productIndex = products.findIndex(p => p.id === productId);
    if (productIndex === -1) {
        console.log("❌ THẤT BẠI: Không tìm thấy sản phẩm.");
        return;
    }

    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question("Xác nhận xóa (y/n): ", (answer) => {
        if (answer.toLowerCase() !== "y") {
            console.log("⚠️ Thao tác xóa đã bị hủy.");
            rl.close();
            return;
        }

        const deleted = products.splice(productIndex, 1);
        console.log(`✅ Đã xóa sản phẩm ${deleted[0].name}`);

        console.log("\nDanh sách sản phẩm còn lại:");
        console.log(products);

        rl.close();
    });
}

// Role hiện tại
const currentRole = "Admin";

// Chạy thử
deleteProductProcess(102, currentRole);

