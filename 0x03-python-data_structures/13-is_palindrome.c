int is_palindrome(listint_t **head) {
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *temp;

    if (*head == NULL || (*head)->next == NULL) {
        return (1);  // An empty list or a list with only one element is a palindrome
    }

    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;
        temp = slow;
        slow = slow->next;
        temp->next = prev;
        prev = temp;
    }

    if (fast != NULL) {
        slow = slow->next;
    }

    while (prev != NULL) {
        if (prev->n != slow->n) {
            return (0);  // It's not a palindrome
        }
        prev = prev->next;
        slow = slow->next;
    }

    return (1);  // It's a palindrome
}
