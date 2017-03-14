/*
 *  Copyright © 2002 Christophe Fergeau
 *  Copyright © 2003 Marco Pesenti Gritti
 *  Copyright © 2003, 2004 Christian Persch
 *    (ephy-notebook.c)
 *
 *  Copyright © 2008 Free Software Foundation, Inc.
 *    (nautilus-notebook.c)
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2, or (at your option)
 *  any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program; if not, see <http://www.gnu.org/licenses/>.
 *
 */

#ifndef NAUTILUS_NOTEBOOK_H
#define NAUTILUS_NOTEBOOK_H

#include <glib.h>
#include <gtk/gtk.h>

typedef struct _NautilusNotebookClass	NautilusNotebookClass;
typedef struct _NautilusNotebook	NautilusNotebook;
typedef struct _NautilusNotebookPrivate	NautilusNotebookPrivate;

#include "nautilus-window-slot.h"

G_BEGIN_DECLS

#define NAUTILUS_TYPE_NOTEBOOK		(nautilus_notebook_get_type ())
#define NAUTILUS_NOTEBOOK(o)		(G_TYPE_CHECK_INSTANCE_CAST ((o), NAUTILUS_TYPE_NOTEBOOK, NautilusNotebook))
#define NAUTILUS_NOTEBOOK_CLASS(k)		(G_TYPE_CHECK_CLASS_CAST((k), NAUTILUS_TYPE_NOTEBOOK, NautilusNotebookClass))
#define NAUTILUS_IS_NOTEBOOK(o)		(G_TYPE_CHECK_INSTANCE_TYPE ((o), NAUTILUS_TYPE_NOTEBOOK))
#define NAUTILUS_IS_NOTEBOOK_CLASS(k)	(G_TYPE_CHECK_CLASS_TYPE ((k), NAUTILUS_TYPE_NOTEBOOK))
#define NAUTILUS_NOTEBOOK_GET_CLASS(o)	(G_TYPE_INSTANCE_GET_CLASS ((o), NAUTILUS_TYPE_NOTEBOOK, NautilusNotebookClass))

struct _NautilusNotebook
{
	GtkNotebook parent;

	/*< private >*/
        NautilusNotebookPrivate *priv;
};

struct _NautilusNotebookClass
{
        GtkNotebookClass parent_class;

	/* Signals */
	void	 (* tab_close_request)  (NautilusNotebook *notebook,
					 NautilusWindowSlot *slot);
};

GType		nautilus_notebook_get_type		(void);

int		nautilus_notebook_add_tab	(NautilusNotebook *nb,
						 NautilusWindowSlot *slot,
						 int position,
						 gboolean jump_to);
	
void		nautilus_notebook_sync_tab_label (NautilusNotebook *nb,
						  NautilusWindowSlot *slot);
void		nautilus_notebook_sync_loading   (NautilusNotebook *nb,
						  NautilusWindowSlot *slot);

void		nautilus_notebook_reorder_current_child_relative (NautilusNotebook *notebook,
								  int offset);
gboolean        nautilus_notebook_can_reorder_current_child_relative (NautilusNotebook *notebook,
								      int offset);
void            nautilus_notebook_prev_page (NautilusNotebook *notebook);
void            nautilus_notebook_next_page (NautilusNotebook *notebook);


G_END_DECLS

#endif /* NAUTILUS_NOTEBOOK_H */

