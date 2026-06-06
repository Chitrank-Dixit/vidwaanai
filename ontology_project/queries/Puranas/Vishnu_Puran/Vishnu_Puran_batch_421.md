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

### Verse 1 (Vishnu Puran 0.8401)
- **Original**: शान्तनुस्तु महोीपाल्लेईभूत्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8402)
- **Original**: अय॑ च तस्य इलोकः पृथ्ििव्यां गीयते
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8403)
- **Original**: हुए, तथा जहूके सुरथ नामक एक पुत्र हुआ
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8404)
- **Original**: सुरथके विदृर्थका जन्म हुआ। बिदूरथके स्ार्वभौम, सार्वभौमके जयत्सेन, जयत्सेनके आयधित, आयधितके अयुतायु, अयुतायुके अक्रोधन, अक्रोधनके देवातिथि तथा देवातिथिके [ अजमीढके पुत्र ऋक्षसे भिन्न ] दूसरे ऋक्षका जन्म हुआ
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8405)
- **Original**: ऋक्षसे भीमसेन, भीमसेनसे दिलीप और दिल्मैपसे प्रतीपनामक पुत्र हुआ
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8406)
- **Original**: अ्रतीपके देवापि, शात्तन्‌ और बाह्लीक नामक तीन पुत्र हुए
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8407)
- **Original**: इनमेंसे देवापि बाल्यावस्थामें ही वनमें चलता गया था अतः चान्तनु ही राजा हुआ। 10-11
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8408)
- **Original**: उसके विषयमें पृथिवीतलपर यह दल्त्रेक कहा जाता है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8409)
- **Original**: आ* 20 ] य॑ य॑ कराभ्यां स्पृश्गति जीर्ण यौवनमेति सः । चतुर्थ अंज् 293 “[ राजा शान्तन्‌ ) जिसको-जिसको अपने हाथसे जान्तिचाप्रोति येनाग्र्यां कर्मणा तेन शान्तनुः
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8410)
- **Original**: स्र्श कर देते थे के वृद्ध पुरुष भी युवानस्था प्राप्त कर लेते तस्थ च शान्तनो राष्ट्रे ्वादशवर्षाणि देवो न वर्ष
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8411)
- **Original**: ततश्चाशेषराष्ट्रविनाझमवेक्ष्यासौ राजा ब्राह्मणानपृच्छत्‌ कस्मादस्माकं राष्ट्रे देवो न वर्षति को ममापराध इति
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8412)
- **Original**: ततश्न तमूचुब्राहिणाः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8413)
- **Original**: अग्रजस्थ ते हीयमवनिस्त्वया सम्भुज्यते अतः: परिवेत्ता ल्वमित्युक्तस्स राजा पुनस्तानपृच्छत्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8414)
- **Original**: कि मयाजत्र विधेयमिति
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8415)
- **Original**: ततस्ते पुनरष्यूचु:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8416)
- **Original**: 19 ।। यावहेवापिर्न पतनादिभिदोषेरभिभूयते तावदेतत्तस्थाई राज्यम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8417)
- **Original**: तदलपेतेन तु तस्मैं दीयतामित्युक्ते तस्य मन्ह्रिप्रवरेणाइमसारिणातत्रारण्ये तपस्विनो : प्रयुक्ता:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8418)
- **Original**: तैरस्थाप्यतिऋजुमतेर्महीपतिपुत्रस्य बुद्धिर्वेद- बादविरोधमार्गानुसारिण्यक्रियत
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8419)
- **Original**: राजा च. शान्लनुर्द्धिजवचनोत्पन्नपरिदेवनशोकस्तान्‌ ब्राह्मणानग्रत:. कृत्वाग्रजस्थ॒ प्रदानायारण्यं जगाम
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8420)
- **Original**: तदाश्रममुपगताक्ष॒ तमवनतमबनीपतिपुत्रं देवापिमुपतस्थु:
- **Translation**: 

---

