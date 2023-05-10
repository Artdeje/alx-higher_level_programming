#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * In this list contains the codes of list.h file.
 * Spaces are for 1 line space.
 * This is Python project codes.
**/

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
