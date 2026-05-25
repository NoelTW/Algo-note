func getSum(a int, b int) int {
    for b != 0 {
        temp_a := a ^ b
        temp_b := (a & b) << 1
        a = temp_a
        b = temp_b
    }
    return a
}
