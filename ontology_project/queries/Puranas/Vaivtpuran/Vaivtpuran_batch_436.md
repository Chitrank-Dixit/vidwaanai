# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Vaivtpuran 23.1682)
- **Original**: तेल उपयोगमें लाया जाय तो उत्तम है। भोजन तथा पीनेसे शेष रहा जूठा जल--ये सब अमावास्या, पूर्णिमा, संक्रान्ति, चतुर्दशी और सर्वथा निधिद्ध हैं। कार्तिकर्में बैंगगका फल,
- **Translation**: 

---

### Verse 2 (Vaivtpuran 23.1683)
- **Original**: अष्टमी तिथियोंमें, रविवारको, श्राद्ध और ब्रतके माघमें मूली तथा श्रीहरिके शवनकाल (चौमासे)-
- **Translation**: 

---

### Verse 3 (Vaivtpuran 23.1684)
- **Original**: दिन स्त्री-सहवास तथा तिलके तेलका सेवन में कलम्बी'का शाक सर्वथा नहीं खाना चाहिये। निषिद्ध है। सभी वर्णोंके लिये दिनमें अपनी सफेद ताड़, मसूर और मछली-ये सभी
- **Translation**: 

---

### Verse 4 (Vaivtpuran 23.1685)
- **Original**: स्त्रीका भी सेवन वर्जित है। रातमें दही खाना, ब्राह्मणोंके लिये समस्त देशोंमें त्वाज्य हैं। दिनमें दोनों संध्याओंके समय सोना तथा प्रतिपदाको कृष्माण्ड (कोहड़ा) नहीं खाना
- **Translation**: 

---

### Verse 5 (Vaivtpuran 23.1686)
- **Original**: रजस्वला स्त्रीके साथ समागम करना--ये नरककी चाहिये; क्योंकि उस दिन वह अर्थका नाश
- **Translation**: 

---

### Verse 6 (Vaivtpuran 23.1687)
- **Original**: प्राप्तिकि कारण हैं। रजस्वला तथा कुलटाका अन्न करनेवाला है। द्वितीयाकों बृहती (छोटे बैंगन
- **Translation**: 

---

### Verse 7 (Vaivtpuran 23.1688)
- **Original**: नहीं खाना चाहिये। अथवा कटेहरी) भोजन कर ले तो उसके दोषसे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 23.1689)
- **Original**: ब्रह्मघें ! शूद्रजातीय स्त्रीसे सम्बन्ध रखनेवाले छुटकारा पानेके लिये श्रीहरिका स्मरण करना
- **Translation**: 

---

### Verse 9 (Vaivtpuran 23.1690)
- **Original**: ब्राह्मणका अन्न भी खाने योग्य नहीं है। ब्रह्मन्‌! चाहिये। तृतीयाकों पघ्घल शत्रुओंकी वृद्धि
- **Translation**: 

---

### Verse 10 (Vaivtpuran 23.1691)
- **Original**: [सूदखोर और गणकका अन्न भी नहीं खाना करनेवाला होता है; अत: उस दिन उसे नहीँ
- **Translation**: 

---

### Verse 11 (Vaivtpuran 23.1692)
- **Original**: चाहिये। अग्रदानी ब्राह्मण (महापात्र) तथा चिकित्सक खाना चाहिये। चतुर्थीकों भोजनके उपयोगमें
- **Translation**: 

---

### Verse 12 (Vaivtpuran 23.1693)
- **Original**: (वैद्य या डाक्टर)-का अन्न भी खाने योग्य नहीं लायी हुई मूली धनका नाश करनेवाली होती
- **Translation**: 

---

### Verse 13 (Vaivtpuran 23.1694)
- **Original**: है। अमावास्या तिथि और कृत्तिका नक्षत्रमें द्विजोंके है। पञ्ममीको बेल खाना कलड्ढू लगनेमें कारण
- **Translation**: 

---

### Verse 14 (Vaivtpuran 23.1695)
- **Original**: लिये क्षौर-कर्म (हजामत) वर्जित है। जो मैथुन होता है। पष्ठीकों नोमकी पत्ती चबायी जाय या
- **Translation**: 

---

### Verse 15 (Vaivtpuran 23.1696)
- **Original**: करके देवताओं तथा पितरोंका तर्पण करता है, उसका फल या दाँतुन मुँहमें डाला जाव तो उसका वह जल रक्तके समान होता है तथा उसे उस पापसे मनुष्यकों पशु-पक्षियोंकी योनिमें जन्म देनेवाला नरकमें पड़ता है। नारद! जो करना लेना पड़ता है। सप्तमीको ताड़का फल खाया
- **Translation**: 

---

### Verse 16 (Vaivtpuran 23.1697)
- **Original**: चाहिये, जो नहीं करना चाहिये, जो भक्ष्य है और जाय तो वह रोग बढ़ानेवाला तथा शरोरका
- **Translation**: 

---

### Verse 17 (Vaivtpuran 23.1698)
- **Original**: जो अभक्ष्य है, वह सब तुम्हें बताया गया। अब नाशक होता है। अष्टमीको नारियलका फल
- **Translation**: 

---

### Verse 18 (Vaivtpuran 23.1699)
- **Original**: और क्या सुनना चाहते हो? (अध्याय 27) #+ल--- 4222 0/:/00005 1. जलज शाकविशेष अथवा कदम्ब।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 23.1700)
- **Original**: परब्नह्म परमात्माके स्वरूपका निरूपण नारदजीने पूछा--जगन्नाथ ! जगदुगे! आपकी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 23.1701)
- **Original**: करनेके लिये सर्वोत्तम प्रदीपके समान है। सनातन कृपासे मैंने सब कुछ सुन लिया। अब आप
- **Translation**: 

---

