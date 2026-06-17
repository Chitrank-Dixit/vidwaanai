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

### Verse 1 (Vaivtpuran 0.81)
- **Original**: करते हैं तथा जो परात्पर-रूप है। शौनकजी! (5 #
- **Translation**: 

---

### Verse 2 (Vaivtpuran 0.82)
- **Original**: वैष्णव, योगी और अन्य संत महात्मा एक-दूसरेसे #6
- **Translation**: 

---

### Verse 3 (Vaivtpuran 0.83)
- **Original**: भिन्न नहीं हैं। जीवधारी मनुष्य अपने ज्ञानके (6 । परिणामस्वरूप क्रमशः संत, योगी और वैष्णव होते हैं। सत्संगसे मनुष्य संत होते हैं। योगियोंके संगसे योगी होते हैं तथा भक्तोंके संगसे वैष्णव
- **Translation**: 

---

### Verse 4 (Vaivtpuran 0.84)
- **Original**: होते हैं। ये क्रमशः उत्तरोत्तर श्रेष्ठ योगी हैं। ब्रह्मखण्डके अनन्तर प्रकृतिखण्ड है, जिसमें किलर 2. 52% जल 0885-02 »
- **Translation**: 

---

### Verse 5 (Vaivtpuran 0.85)
- **Original**: देवताओं, देवियों और सम्पूर्ण जीवोंकी उत्पत्तिका उपस्थित देख नमस्कार करनेके लिये चला
- **Translation**: 

---

### Verse 6 (Vaivtpuran 0.86)
- **Original**: कथन है। साथ ही देवियोंके शुभ चरित्रका वर्णन आया हूँ। साथ ही भारतवर्षके पुण्यदायक क्षेत्र
- **Translation**: 

---

### Verse 7 (Vaivtpuran 0.87)
- **Original**: है। जीवोंके कर्मविपाक और शालग्राम-शिलाके नैमिषारण्यका दर्शन भी मेरे यहाँ आगमनका
- **Translation**: 

---

### Verse 8 (Vaivtpuran 0.88)
- **Original**: महत्त्वका निरूपण है। उन देवियोंके कबच, उद्देश्य है। जो देवता, ब्राह्मण और गुरुको देखकर
- **Translation**: 

---

### Verse 9 (Vaivtpuran 0.89)
- **Original**: स्तोत्र, मन्त्र और पूजा-पद्धतिका भी प्रतिपादन बेगपूर्वक उनके सामने मस्तक नहीं झुकाता है,
- **Translation**: 

---

### Verse 10 (Vaivtpuran 0.90)
- **Original**: किया गया है। उस प्रकृतिखण्डमें प्रकृतिके वह “कालसूत्र' नामक नरकमें जाता है तथा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 0.91)
- **Original**: लक्षणका वर्णन है। उसके अंशों और कलाओंका जबतक चन्रमा और सूर्यवकी सत्ता रहती है,
- **Translation**: 

---

### Verse 12 (Vaivtpuran 0.92)
- **Original**: निरूपण है। उनकी कीर्तिका कीर्तन तथा तबतक वह वहीं पड़ा रहता है। साक्षात्‌ श्रीहरि
- **Translation**: 

---

### Verse 13 (Vaivtpuran 0.93)
- **Original**: प्रभावका प्रतिपादन है। पुण्यात्माओं और पापियोंको ही भारतवर्षमें ब्राह्मणरूपसे सदा भ्रमण करते
- **Translation**: 

---

### Verse 14 (Vaivtpuran 0.94)
- **Original**: जो-जो शुभाशुभ स्थान प्राप्त होते हैं, उनका वर्णन रहते हैं। श्रीहरि-स्वरूप उस ब्राह्मणको कोई
- **Translation**: 

---

### Verse 15 (Vaivtpuran 0.95)
- **Original**: है। पापकर्मसे प्राप्त होनेवाले नरकों तथा रोगोंका पुण्यात्मा ही अपने पुण्यके प्रभावसे प्रणाम करता
- **Translation**: 

---

### Verse 16 (Vaivtpuran 0.96)
- **Original**: कथन है। उनसे छूटनेके उपायका भी विचार है। भगबन्‌ ! आपने जो कुछ पूछा है तथा आपको
- **Translation**: 

---

### Verse 17 (Vaivtpuran 0.97)
- **Original**: किया गया है। जो कुछ जानना अभीष्ट है, वह सब आपको प्रकृतिखण्डके पश्चात्‌ गणेशखण्डमें गणेशजीके पहलेसे ही ज्ञात है, तथापि आपकी आज्ञा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 0.98)
- **Original**: जन्मका वर्णन है। उनके उस अत्यन्त अपूर्ब शिरोधार्य कर मैं इस विषयमें कुछ निबेदन करता
- **Translation**: 

---

### Verse 19 (Vaivtpuran 0.99)
- **Original**: चरित्रका निरूपण है, जो श्रुतियों और वेदोंके हूँ। पुराणोंमें सारभूत जो ब्रह्मवैवर्त नामक पुराण
- **Translation**: 

---

### Verse 20 (Vaivtpuran 0.100)
- **Original**: लिये भी परम दुर्लभ है। गणेश और भृगुजोके है, वही सबसे उत्तम है। वह हरिभक्ति देनेवाला
- **Translation**: 

---

