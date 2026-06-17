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

### Verse 1 (Vishnu Puran 0.2781)
- **Original**: 17 ये तु देबाधिपतयो ये च॒ दैत्याधिपास्तथा । दानवानां च ये नाथा ये नाथा: पिशिताशिनाम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2782)
- **Original**: 18 पश्चूतां ये च फ्तय: पतयो ये च पक्षिणाम्‌ । मनुष्याणां चर सर्पाणों नागानामधिपाश्ष ये
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2783)
- **Original**: 19 वृक्षाणां पर्वतानां च ग्रहार्णा चापि येडधिपा: । अतीता वर्त्तमानाक्ष ये भविष्यन्ति चापरे
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2784)
- **Original**: ते सर्वे सर्वभूतस्य विष्णोरंशसमुद्धवाः
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2785)
- **Original**: 20 न॒ हि पालनसामर्थ्यमृते सर्वेश्वरं हरिम्‌। स्थित स्थितों महाप्राज्ञ मवत्यन्यस्थ कस्यचित्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2786)
- **Original**: 29 चतुर्विभाग: संसृष्टो चतुर्धा संस्थितः स्थितो । प्रकयं च करोत्यन्ते चतुर्भेंदी जनार्दन:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2787)
- **Original**: 23 एकेनांशेन ब्रह्मासो भवत्यव्यक्तमूर्त्तिमान्‌। मरीचिमिश: पतय:ः प्रजानां चान्यभागश:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2788)
- **Original**: 24 कालस्तृतीयस्तस्यांश: सर्वभूतानि चापर: । इत्थ॑ चतुर्धा संसुष्टी वर्त्तीऔइसों रजोगुण:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2789)
- **Original**: 25 एकांशेनास्थितो विष्णु: करोति प्रतिपालनम्‌। मन्वादिरूप श्रान्येन कालरूपोउपरेण च
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2790)
- **Original**: 26 सतत गुणं समाश्रित्य जगत: पुरुषोत्तम:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2791)
- **Original**: 27 आश्रित्य तमसो वृत्तिमन्तकाले तथा पुनः । स्द्वस्वरूपो भगवानेकांशेन भवत्यज:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2792)
- **Original**: 28 अम्न्यन्तकादिरूपेण भागेनान्येन वर्त्तते । कालस्वरूपो भागो यस्सर्वभूतानि चापर:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2793)
- **Original**: 29 बिनाझं कुर्वतस्तस्य चतुर्द्धव॑ पहात्मन: । बिभागकल्पना ब्रह्मन्‌ कथ्यते सार्वकालिकी
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2794)
- **Original**: 30 ब्रह्मा दक्षादयः कालस्तथैबाखिलजन्तवः । विभूतयो हरेरेता जगतः सृष्टिहेतवः
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2795)
- **Original**: 39 है मुनिसत्तम
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2796)
- **Original**: ! ये तथा अन्य भी जो सम्पूर्ण राजात्म्रेग हैं जे सभी विश्वके पालनमें प्रवत्त परमात्मा श्रीलिष्णुभगजानके विभूतिरूप हैं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2797)
- **Original**: हे ट्विजोत्तम ! जो-जो भूताधिपति पहले हो गये हैं और जो-जो आगे होंगे त्षे सभी सर्वभूत भगवान्‌ विष्णुके अंझ हैं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2798)
- **Original**: जो-जो भी देवताओं, दैत्यों, दानवों और मांसभोजियोॉंके अधिपति है, जो-जो पशुओं, पक्षियों, मनुष्यों, सर्पों और नागेकि अधिनायक हैं, जो जो बृक्षों, पर्वतों और ग्रहोंके स्तामो हैं तथा और भी चूत, भविष्यत्‌ एवं वर्तमानकालीन जितने भूतेश्वर हैं ये सभी सर्वभूत भगवान्‌ विष्णुके अंडासे उत्पन्न हुए हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2799)
- **Original**: 18--20
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2800)
- **Original**: है महाप्राज्ञ ! सृष्टिके पालन- कार्यमें प्रवृत्त सर्वे्षर श्रीहरिको छोड़कर और किसीमें भी पालन करनेकी दाक्ति नहीं है
- **Translation**: 

---

