int is_palindrome(listint_t **head) {
    listint_t *slow = *head;  /* Initialize slow pointer at the head of the list */
    listint_t *fast = *head;  /* Initialize fast pointer at the head of the list */
    listint_t *prev = NULL;    /* Initialize a pointer to reverse the first half of the list */
    listint_t *temp;           /* Temporary pointer */

    if (*head == NULL || (*head)->next == NULL)
    {
        return (1);  /* An empty list or a list with only one element is a palindrome */
    }

    while (fast != NULL && fast->next != NULL)
    {
        /* Move fast two steps and slow one step */
        fast = fast->next->next;

        /* Reverse the first half of the list */
        temp = slow;
        slow = slow->next;
        temp->next = prev;
        prev = temp;
    }

    if (fast != NULL)
    {
        slow = slow->next;  /* If the list has an odd number of elements, adjust slow */
    }

    while (prev != NULL)
    {
        if (prev->n != slow->n) {
            return (0);  /* It's not a palindrome */
        }
        prev = prev->next;
        slow = slow->next;
    }

    return (1);  /* It's a palindrome */
}
