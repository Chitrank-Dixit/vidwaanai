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

### Verse 1 (Sama Ved 0.1321)
- **Original**: पूर्वार्चिकि पावमानपर्वोणि पञ्लमो ख्याय: 5.5 7505, डृषे पवस्व धारया मृज्यमानों मनीषिभिः । इन्दो रुचाभि गा इहि
- **Translation**: 

---

### Verse 2 (Sama Ved 0.1322)
- **Original**: . हे सोम ! आप ज्ञानी ऋत्थिजों के ड्रारा अभिषुत होकर पोषक रस के लिए धारा के रूप में शुद्ध हों और गोदुग्ध के साथ मिलकर प्रकाशित हों
- **Translation**: 

---

### Verse 3 (Sama Ved 0.1323)
- **Original**: 506. मन्द्रया सोम धारया वृषा पवस्व देवयु: । अव्या वारेभिरस्मयु:
- **Translation**: 

---

### Verse 4 (Sama Ved 0.1324)
- **Original**: बलवर्द्धक, देवताओं द्वारा अभी हे सोम ! आप हमें संरक्षण प्रदान करें और छननी में आनन्ददायक धारा के रूप में शोधित हों
- **Translation**: 

---

### Verse 5 (Sama Ved 0.1325)
- **Original**: 507. अया सोम सुकृत्यया महान्त्सन्नभ्यवर्धथा: । मन्दान इृद्‌ वृषायसे
- **Translation**: 

---

### Verse 6 (Sama Ved 0.1326)
- **Original**: है सोमदेव ! आप अपने श्रेष्ठ कार्य से सम्माननीय होकर, महानता को प्राप्त करते हैं और आनन्द प्रदान कर शक्ति बढ़ाते हैं
- **Translation**: 

---

### Verse 7 (Sama Ved 0.1327)
- **Original**: 508, अय॑ विचर्षणिहितः पवमान: स चेतति
- **Translation**: 

---

### Verse 8 (Sama Ved 0.1328)
- **Original**: हिन्वान आप्यं बृहत्‌
- **Translation**: 

---

### Verse 9 (Sama Ved 0.1329)
- **Original**: विशिष्ट बुद्धिवर्द्धक, बर्तन में स्थित होकर शुद्ध किया हुआ, यह सोमरस पानी में मिलकर प्रचुर अन्न (पोषण) प्रदान करता छुआ यशस्वी होता है
- **Translation**: 

---

### Verse 10 (Sama Ved 0.1330)
- **Original**: 509.प्र न इन्दो महे तु न ऊर्मि न बिश्रदर्षसि । अभि देवाँ अयास्य:
- **Translation**: 

---

### Verse 11 (Sama Ved 0.1331)
- **Original**: हे सोम ! प्रचुर सम्पदा की प्राप्ति के लिए आप कलश में छाने जाते हैं । आपके तेज को धारण करने वाले अयास्य त्रद्रषि देव पूजन (देवत्व को घारण) करते हैं
- **Translation**: 

---

### Verse 12 (Sama Ved 0.1332)
- **Original**: 510.अपध्नन्यवते मृधो5प सोमो अराग्ण:
- **Translation**: 

---

### Verse 13 (Sama Ved 0.1333)
- **Original**: गच्छन्निन्द्रस्य निष्कृतम्‌
- **Translation**: 

---

### Verse 14 (Sama Ved 0.1334)
- **Original**: यह सोम रिपुओं को तथा दान + देने वालों को मारता है । इन्द्रदेव के पास जाता हुआ क्षरित होता है
- **Translation**: 

---

### Verse 15 (Sama Ved 0.1335)
- **Original**: इति चतुर्थ: खण्ड:
- **Translation**: 

---

### Verse 16 (Sama Ved 0.1336)
- **Original**: के के के
- **Translation**: 

---

### Verse 17 (Sama Ved 0.1337)
- **Original**: पंचम: खण्ड:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.1338)
- **Original**: 5161. पुनान: सोम धारयापो वसानो अर्पसि। आ रलथा योनिमृतस्य सीदस्युत्सो देवो हिरण्यय:
- **Translation**: 

---

### Verse 19 (Sama Ved 0.1339)
- **Original**: सोमरस पवित्र होकर, जल में मिलकर, धारा सहित नीचे कलश में प्रवाहित होता है । रत्मादि देने बाला, यज्ञमण्डप में आसीन, आलोकित होता हुआ, वह सोमरस प्रवाहित होता है
- **Translation**: 

---

### Verse 20 (Sama Ved 0.1340)
- **Original**: 512.परीतो षिज्चता सुतं सोमो य उत्तम॑ हविः । दधन्वाँ यो नयों अप्स्वा3न्तरा सुधाव सोममद्रिभि:
- **Translation**: 

---

