# -*- coding: utf-8 -*-

# Inscrisup - Gestion des inscriptions administratives après Parcoursup
# Copyright (c) 2018 Florian Hatat
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from __future__ import unicode_literals

from odf.opendocument import OpenDocumentSpreadsheet
from odf.table import Table, TableColumn, TableRow, TableCell
from odf.style import Style, TableColumnProperties, TableRowProperties, \
        TextProperties, ParagraphProperties
import odf.number
from odf.text import P

def par_classe(classes, fileout):
    ods = OpenDocumentSpreadsheet()

    style_civilite = Style(parent=ods.automaticstyles,
            name='col_civilite', family='table-column')
    TableColumnProperties(parent=style_civilite, columnwidth='1cm')

    style_nom = Style(parent=ods.automaticstyles,
            name='col_nom', family='table-column')
    TableColumnProperties(parent=style_nom, columnwidth='4.5cm')

    style_date = Style(parent=ods.automaticstyles,
            name='col_date', family='table-column')
    TableColumnProperties(parent=style_date, columnwidth='3.2cm')

    style_etat_voeu = Style(parent=ods.automaticstyles,
            name='col_etat_voeu', family='table-column')
    TableColumnProperties(parent=style_etat_voeu, columnwidth='4cm')

    style_titre = Style(parent=ods.automaticstyles,
            name='cell_titre', family='table-cell')
    TextProperties(parent=style_titre, fontweight='bold',
            fontsize='14pt')
    ParagraphProperties(parent=style_titre, textalign='center')

    style_ligne_titre = Style(parent=ods.automaticstyles,
            name='ligne_titre', family='table-row')
    TableRowProperties(parent=style_ligne_titre, rowheight='8mm')

    style_entete = Style(parent=ods.automaticstyles,
            name='cell_entete', family='table-cell')
    TextProperties(parent=style_entete, fontweight='bold')

    number_style_date_format = odf.number.DateStyle(parent=ods.automaticstyles,
            name='date_number')
    odf.number.Day(parent=number_style_date_format, style='long')
    odf.number.Text(parent=number_style_date_format, text="/")
    odf.number.Month(parent=number_style_date_format, style='long')
    odf.number.Text(parent=number_style_date_format, text="/")
    odf.number.Year(parent=number_style_date_format, style='long')
    style_date_format = Style(parent=ods.automaticstyles,
            name='cell_date', family='table-cell',
            datastylename=number_style_date_format)

    for classe in classes:
        table = Table(name=str(classe))
        table.addElement(TableColumn(stylename=style_civilite)) # Sexe
        table.addElement(TableColumn(stylename=style_nom)) # Nom
        table.addElement(TableColumn(stylename=style_nom)) # Prénom
        table.addElement(TableColumn(stylename=style_date)) # Date de naissance
        table.addElement(TableColumn()) # Internat
        table.addElement(TableColumn(stylename=style_etat_voeu)) # État vœu

        # En-tête de la feuille
        tr = TableRow(parent=table, stylename=style_ligne_titre)
        cell = TableCell(parent=tr, numbercolumnsspanned=6,
                stylename=style_titre)
        cell.addElement(P(text=str(classe)))

        tr = TableRow(parent=table)
        TableCell(parent=tr) # Sexe
        P(parent=TableCell(parent=tr, stylename=style_entete), text="Nom")
        P(parent=TableCell(parent=tr, stylename=style_entete), text="Prénom")
        P(parent=TableCell(parent=tr, stylename=style_entete), text="Date de naissance")
        P(parent=TableCell(parent=tr, stylename=style_entete), text="Internat")
        P(parent=TableCell(parent=tr, stylename=style_entete), text="État Parcoursup")

        for etudiant in classe.admissions().order_by('nom'):
            tr = TableRow()
            table.addElement(tr)

            TableCell(parent=tr).addElement(P(text=etudiant.get_sexe_display()))

            TableCell(parent=tr).addElement(P(text=etudiant.nom))

            TableCell(parent=tr).addElement(P(text=etudiant.prenom))

            cell = TableCell(valuetype='date',
                    datevalue=str(etudiant.date_naissance),
                    stylename=style_date_format)
            cell.addElement(P(text=etudiant.date_naissance))
            tr.addElement(cell)

            cell = TableCell()
            if etudiant.proposition_actuelle.internat:
                cell.addElement(P(text="Interne"))
            tr.addElement(cell)

            TableCell(parent=tr).addElement(P(text=etudiant.proposition_actuelle.get_statut_display()))

        ods.spreadsheet.addElement(table)

    ods.write(fileout)
