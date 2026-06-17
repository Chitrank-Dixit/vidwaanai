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

### Verse 1 (Rig Ved 0.1)
- **Original**: ऋग्वेद - संहिता के मे नर
- **Translation**: 

---

### Verse 2 (Rig Ved 0.2)
- **Original**: अथ प्रथम मण्डलम्‌
- **Translation**: 

---

### Verse 3 (Rig Ved 0.3)
- **Original**: [सूक्त - 1
- **Translation**: 

---

### Verse 4 (Rig Ved 0.4)
- **Original**: [अर्प्षि- मधुच्छन्दा वैश्वामित्र
- **Translation**: 

---

### Verse 5 (Rig Ved 0.5)
- **Original**: देवता - अग्नि ! छन्द्‌-गायत्री] 1. 3» अम्निमील्े पुरोहितं यज्ञस्थ देवमृत्विजम्‌। होतारं रत्मनधातमम्‌
- **Translation**: 

---

### Verse 6 (Rig Ved 0.6)
- **Original**: हम अग्निदेव की स्तुति करते हैं
- **Translation**: 

---

### Verse 7 (Rig Ved 0.7)
- **Original**: (कैसे अग्निदेव ?) जो यज्ञ (श्रेष्ठतम पारमार्थिक कर्म) के पुरोहित (आगे बढ़ाने वाले) देवता (अनुदान देने वाले), ऋत्विज्‌ (समयानुकूल यज्ञ का सम्पादन करने वाले), होता (देवों का आवाहन करने वाले) और बाजकों को रलों से (यज्ञ के लाभों से) विधूषित करने वाले हैं
- **Translation**: 

---

### Verse 8 (Rig Ved 0.8)
- **Original**: 2. अग्नि: पूर्वेभिऋषिभिरीड्यों नूतनेरुत। स देवाँ एह वक्षति
- **Translation**: 

---

### Verse 9 (Rig Ved 0.9)
- **Original**: जो अग्निदेव पूर्वकालीन ऋषियों (भृगु, अंगिरादि) द्वारा प्रशंसित हैं । जो आधुनिक काल में भी ऋषि कल्प बेदज्ञ विद्ानों द्वारा स्तुत्य हैं, वे अग्निदेव इस यज्ञ में देवों का आवाहन करें
- **Translation**: 

---

### Verse 10 (Rig Ved 0.10)
- **Original**: 3. अग्निना रयिमश्लवत्‌ पोषमेव दिवेदिवे । यशसं बीरवत्तमम्‌
- **Translation**: 

---

### Verse 11 (Rig Ved 0.11)
- **Original**: (स्तोता द्वारा स्तुति किये जाने पर) ये बढ़ाने वाले अग्निदेव मनुष्यों (बजमानों) को प्रतिदिन विवर्धमान (बढ़ने चाला ) धन, यश एवं पुत्र-पौव्रादि वीर पुरुष प्रदान करने वाले हैं
- **Translation**: 

---

### Verse 12 (Rig Ved 0.12)
- **Original**: 4. अने य॑ यज्ञमध्वरं विश्वत: परिभूरसि। स इद्देवेषु गच्छति
- **Translation**: 

---

### Verse 13 (Rig Ved 0.13)
- **Original**: है अग्निदेव ! आप सयका रक्षण करने में समर्थ हैं । आप जिस अध्यर (हिंसारहित यज्ञ) को सभी ओर से आवृत किये रहते हैं, वही यज्ञ देवताओं तक पहुँचता है
- **Translation**: 

---

### Verse 14 (Rig Ved 0.14)
- **Original**: 5. अमभिनहोंता कविक्रतुः सत्यश्चित्रश्रवस्तम:
- **Translation**: 

---

### Verse 15 (Rig Ved 0.15)
- **Original**: देवो देवेभिरा गमत्‌
- **Translation**: 

---

### Verse 16 (Rig Ved 0.16)
- **Original**: है अग्निदिव ! आप हवि -प्रदाता, ज्ञान और कर्म की संयुवत शवित के प्रेरक, सत्यरूप एवं विलक्षण रूप युक्त हैं। आप देवों के साथ इस यज्ञ में पधारें
- **Translation**: 

---

### Verse 17 (Rig Ved 0.17)
- **Original**: 6. यदड् दाशुषे त्वमग्ने भद्रं करिष्यसि। तवेत्तत्‌ सत्यमड्विर:
- **Translation**: 

---

### Verse 18 (Rig Ved 0.18)
- **Original**: है अग्निदेव ! आप यज्ञ करने वाले यज़मान का धन, आवास, संतान एवं पशुओं की समृद्धि करके जो भी कल्याण करते हैं, बह भविष्य में किये जाने वाले यज्ञों के माध्यम से आपको ही प्राप्त होता है ।
- **Translation**: 

---

### Verse 19 (Rig Ved 0.19)
- **Original**: 2 ऋत!वेद संहिता भाग-9 7. उप त्वाग्ने दिवेदिवे दोषावस्तर्थिया वयम्‌। नमो भरन्त एमसि
- **Translation**: 

---

### Verse 20 (Rig Ved 0.20)
- **Original**: हे जाज्वल्यमान अग्निदेव ! हम आपके सच्चे उपासक हैं । श्रेष्ठ बुद्धि द्वारा आपकी स्तुति करते हैं और दिन-रात, आपका सतत गुणगान करते हैं
- **Translation**: 

---

