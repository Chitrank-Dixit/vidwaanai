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

### Verse 1 (Rig Ved 0.11501)
- **Original**: है सरस्वती देवि ! आपने देवताओं की निन्‍्दा करने वाले को नष्ट किया । आप उसी तरह कपटी-दुष्टों का नाश करें । मानवों के लाभ के लिए आपने संरक्षित भू-भाग प्रदान किए हैं। हे वाजिनौबत्ति ! आपने हो मनुष्यों के लिए जल प्रवाहित किया है
- **Translation**: 

---

### Verse 2 (Rig Ved 0.11502)
- **Original**: 5005, प्र णो देवी सरस्वती वाजेभिवाजिनीवती
- **Translation**: 

---

### Verse 3 (Rig Ved 0.11503)
- **Original**: धीनामवित््यवतु
- **Translation**: 

---

### Verse 4 (Rig Ved 0.11504)
- **Original**: सरस्वती देवी अमेक प्रकार के अन्न देने से अन्नवाली कहलाती हैं । वे रक्षा करती है । वे देवि हमें उत्तम प्रकार से तृप्त करें
- **Translation**: 

---

### Verse 5 (Rig Ved 0.11505)
- **Original**: 5006. यस्त्या देवि सरस्वत्युपब्ूते धने हिते। इन्द्र न वृत्रतूर्ये
- **Translation**: 

---

### Verse 6 (Rig Ved 0.11506)
- **Original**: जिस भ्रकार इन्धदेव को युद्ध में शत्रुओं से रक्षा करने के निमित्त बुलाते हैं, उसी प्रकार युद्ध के प्रारम्भ के सप्य जो आपका आवाहन करता है, आप उसकी रक्षा करती हैं
- **Translation**: 

---

### Verse 7 (Rig Ved 0.11507)
- **Original**: 5007, त्वं देवि सरस्वत्यवा वाजेबु वाजिनि। रदा पूषेव नः सनिम्‌
- **Translation**: 

---

### Verse 8 (Rig Ved 0.11508)
- **Original**: हे सरस्वती देवि ! आप बल से युक्त हैं । आप संग्राम के समय हमारी रक्षा करें एवं पृषन्‌देव की तरह हमें धन प्रदान करें
- **Translation**: 

---

### Verse 9 (Rig Ved 0.11509)
- **Original**: 5008. उत स्या नः सरस्वती घोरा हिरण्यवर्त नि : । वृत्रघ्नी वष्टि सुष्रुतिम्‌
- **Translation**: 

---

### Verse 10 (Rig Ved 0.11510)
- **Original**: स्वर्णिम रथ पर आरूढ़, प्रचण्ड वीरता धारण करने वाली देवो सरस्वती शत्रुओं का नाश करती हैं और स्तोताओं की रक्षा करती हैं
- **Translation**: 

---

### Verse 11 (Rig Ved 0.11511)
- **Original**: 5009, यस्या अनन्तो अह्लुतस्त्वेषश्षरिष्णुरर्णव :
- **Translation**: 

---

### Verse 12 (Rig Ved 0.11512)
- **Original**: अमश्नरति रोरुवत्‌
- **Translation**: 

---

### Verse 13 (Rig Ved 0.11513)
- **Original**: उन (सरस्वती) का निरन्तर प्रयाहित जल, येग से गमन करता हुआ, गर्जन (शब्द) करता है
- **Translation**: 

---

### Verse 14 (Rig Ved 0.11514)
- **Original**: 5010, सा नो विश्वा अति द्विष: स्वसूरन्या ऋतावरी । अतन्नहेव सूर्य:
- **Translation**: 

---

### Verse 15 (Rig Ved 0.11515)
- **Original**: 86 ऋण्वेद संहिता भाग - 2 जिस प्रकार सूर्यदेव प्रकाश फँलाते हूँ, वैसे ही देवों सरस्वती शत्रुओं को परास्त करतों हुई बहिनों सहित आती हैं
- **Translation**: 

---

### Verse 16 (Rig Ved 0.11516)
- **Original**: 5011. उत नः प्रिया प्रियासु सप्तस्वसा सुजुष्टा। सरस्वती स्तोम्या भूतू 10
- **Translation**: 

---

### Verse 17 (Rig Ved 0.11517)
- **Original**: प्रियजनों में अतिप्रिय, सप्त बहिनों (सात छन्दों अथवा सहायक धाराओं) से युक्त देवी सरस्वती हमारे लिए स्तुत्य हैँ
- **Translation**: 

---

### Verse 18 (Rig Ved 0.11518)
- **Original**: 5012. आपप्ुषी पार्थिवान्युरु रजो अन्तरिक्षम्‌। सरस्वती निदस्पातु
- **Translation**: 

---

### Verse 19 (Rig Ved 0.11519)
- **Original**: जिन देवी सरस्वती ने स्वर्ग और पृथ्वी को अपने तेज से भर दिया है, वे हमें निन्‍्दा करने वालों से बचाएँ
- **Translation**: 

---

### Verse 20 (Rig Ved 0.11520)
- **Original**: 5013, त्रिषधस्था सप्तधातु: पञ्च जाता वर्धयन्ती । बाजेवाजे हव्या भूत्‌
- **Translation**: 

---

