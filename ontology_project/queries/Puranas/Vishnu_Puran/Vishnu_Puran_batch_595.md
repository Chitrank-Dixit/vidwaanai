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

### Verse 1 (Vishnu Puran 0.11881)
- **Original**: 47 निर्यॉवना गतश्रीका नष्टच्छायेव मेदिनी । विभाति तात नैको5हं बिरहे तस्य चक्रिण:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11882)
- **Original**: । 48 यस्य प्रभावाद्धीष्माहरर्मय्यप्नों शलूभायितम्‌। बिना तेनाद्य कृष्णेन गोपालेरस्मि निर्जित:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11883)
- **Original**: 49 गाण्डीवर्त्रिषु लोकेषु ख्याति यदनुभावत: । गतस्तेन बिनाभीरलगुडैस्स तिरस्कृत:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11884)
- **Original**: 50 सत्रीसहस्राण्यनेकानि मन्नाथानि महामुने । यततो मम नीतानि दस्युभिर्लगुडायुथै:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11885)
- **Original**: 51 आनीयमानमाभीर: कृष्ण कृष्णावरो धनम्‌ । हत॑ यपष्टिप्रहएण: परिभूय बलं मम
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11886)
- **Original**: 52 निइश्रीकता न मे चित्र यज्जीवामि तदद्भुतम्‌ । नीचावमानपड़ाड़ी निलज्जोउस्मि पितामह
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11887)
- **Original**: 53 श्रीव्यास उवाच अल ते ब्रीडया पार्थ न त्व॑ झोचितुमहसि । अवेहि सर्वभूतेषु कालस्य गतिरीदृशी
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11888)
- **Original**: 54 कालो भवाय भूतानामभवाय उ पाण्डव । कालमूलमिद ज्ञात्वा भव स्थैर्यपरोईर्जुन
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11889)
- **Original**: 55 तो नहीं पड़ गयीं अथया तुम्हें किसी हीनबल पुरुषने युद्धमें पराजित तो नहीं किया ? फिर तुम इस तरह हतप्रभ कैसे हो रहे हो ?'
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11890)
- **Original**: श्रीपराशरजी बोले--तजत्र अर्जुनने दीर्घ नि:ध्वास छोड़ते हुए वकह्ा--''भगवन्‌ ! सुनिये” ऐसा कहकर ज्यॉ-का-त्यों सुना दिया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11891)
- **Original**: खोले--जो हरि मेंरे एकमात्र बल, त्तेज, वीर्य, पराक्रम, श्री और कान्ति थे वे हमें छोड़कर चक्ते गये
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11892)
- **Original**: जो स्रब प्रकार समर्थ होकर भी हमसे मित्रवत्‌ हैंस-हैसकर बातें किया करते थे, हे मुने ! उन हस्कि बिना हम आज तृणमय पुतलछेके समान निःसन्त्व हो गये हैं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11893)
- **Original**: जो मेरे दिव्यास्त्रों, दिव्यवाणों और गाण्डीव धनुषके मूर्तिमान्‌ सार थे वे पुरुषोत्तम भगवान्‌ हमें छोड़कर चले गये हैं
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11894)
- **Original**: जिनकी कपाटष्टिसे श्री, जय, सम्पत्ति और उन्नतिने कभी हमारा साथ नहीं छोड़ा वे हौ भगवान्‌ गोविंद हमें छोड़कर चले गये हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11895)
- **Original**: जिनकी प्रभावाग्रिमें भीष्म, द्रोण, कर्ण और दुर्योधन आदि अनेकों शूरबोर दग्ध हो गये थे उन कृष्णचद्धने इस भूमण्डल्थ्को छोड़ दिया है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11896)
- **Original**: हे तात ! उन चक्रपाणि कृष्णचन्द्रके विरहमें एक मैं ही क्या, सम्पूर्ण पृथिबी ही यौन, श्री और कान्तिसे हीत प्रतीत होती है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11897)
- **Original**: जिनके प्रभावसे अप्रिरूप मुझमें भीष्म आदि महारथीगण पतंगठत्‌ भस्म हो गये थे, आज उन्हों कृष्णके बिना मुझे गोपोने हरा दिया !
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11898)
- **Original**: जिनके प्रभावसे यह गाण्डीव धनुष तीनों लोकोमें विख्यात हुआ था उन्हींके बिना आज यह अहोरोंकी लाठियोंसे तिरस्कृत हो गया!
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11899)
- **Original**: हे महामुने ! भगवान्‌की जो सहस्नरों स्वियाँ मेरी देख-रेखमें आ रही थीं उन्हें, मेरे सब प्रकार यत्र करते रहनेपर भी दस्युगण अपनी ल्ाठियॉंके बलसे ले गये
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11900)
- **Original**: हे कृष्ण- ड्रैपाथन ! लाठियाँ ही जिनके हथियार हैं उन आभीरोंने आज मेंरे बलको कुण्ठितकर मेरेड्ारा साथ त्थये हुए सम्पूर्ण कृष्ण-परिवारकों हर किया
- **Translation**: 

---

