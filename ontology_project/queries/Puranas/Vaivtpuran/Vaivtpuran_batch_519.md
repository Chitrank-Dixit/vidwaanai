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

### Verse 1 (Vaivtpuran 31.7551)
- **Original**: है। वह शान्तिलाभ करके समस्त सिद्धोंका ईश्वर अवर्णनीय हैं, अत: विद्वान्‌ जिनकी स्तुति करनेमें हो जाता है और अन्तमें श्रीहरिके परमपदको प्राप्त असमर्थ हैं तथा जिनका गुणगान वाक्‌-शक्तिके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 31.7552)
- **Original**: कर लेता है तथा भूतलपर अपने तेज और यशसे बाहर है; भला, उनका स्तवन* करके कौन पार
- **Translation**: 

---

### Verse 3 (Vaivtpuran 31.7553)
- **Original**: सूर्यकी तरह प्रकाशित होता है। वह जीवन्मुक्त,
- **Translation**: 

---

### Verse 4 (Vaivtpuran 31.7554)
- **Original**: *» गणपतिखण्ड « 361 श्रीकृष्णभपक्त, सदा नीरोग, गुणवान्‌, विद्वान,
- **Translation**: 

---

### Verse 5 (Vaivtpuran 31.7555)
- **Original**: बना रहता है। वत्स! इस प्रकार मैंने इस स्तोत्रका पुत्रवान्‌ और धनी हो जाता है--इसमें तनिक भी
- **Translation**: 

---

### Verse 6 (Vaivtpuran 31.7556)
- **Original**: वर्णन कर दिया। अब तुम पुष्करमें जाओ और संशय नहीं है। वह निश्चय ही छहों विषयोंका
- **Translation**: 

---

### Verse 7 (Vaivtpuran 31.7557)
- **Original**: वहाँ मन्त्र सिद्ध करो। तत्पश्चात्‌ तुम्हें अभीष्ट जानकार, दसों बलोंसे सम्पन्न, मनके सदृश
- **Translation**: 

---

### Verse 8 (Vaivtpuran 31.7558)
- **Original**: फलको प्राप्ति होगी। मुनिश्रेष्ठ! यों श्रीकृष्णकी वेगशाली, सर्वज्ञ, सर्वस्व दान करनेवाला और
- **Translation**: 

---

### Verse 9 (Vaivtpuran 31.7559)
- **Original**: कृपासे तथा मेरे आशीर्वादसे तुम सुखपूर्वक सम्पूर्ण सम्पदाओंका दाता हो जाता है तथा
- **Translation**: 

---

### Verse 10 (Vaivtpuran 31.7560)
- **Original**: पृथ्वीको इक्कीस बार क्षत्रियोंसे शून्य करो*। श्रीकृष्णकी कृपासे वह निरन्तर कल्पवृक्षके समान (अध्याय 32) आल * महादेव उवाच-- पर॑ ब्रह्म पर॑ धाम परे ज्योति: सनातनम्‌ । निर्लिम्तं परमात्मानं नमामि सर्वकारणम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 31.7561)
- **Original**: स्थूलात्‌ स्थूलतम देव॑ सूक्ष्मात्‌ सूक्ष्मतम॑ परम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 31.7562)
- **Original**: सर्वदृश्यमदृश्य॑च स्वेच्छाचार॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 31.7563)
- **Original**: साकार॑ च निराकारं सगुणं निर्गुणं प्रभुम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 31.7564)
- **Original**: सर्वाधारं च सर्व॑ च॒ स्वेच्छारूपं नमाम्यहम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 31.7565)
- **Original**: अतीवकमनीय॑ च रूप॑ निरुपम॑ विभुम्‌ । करालरूपमत्यन्तं विध्र्त प्रणमाम्यहम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 31.7566)
- **Original**: कर्मण: कर्मरूप॑ त॑ साक्षिणं. सर्वकर्मणामू । फलं॑ च फलदातार॑ सर्वरूप॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 31.7567)
- **Original**: सन्‍ष्टा पाता च॒ संहर्ता कलया पूर्तिभेदतः । नानामूर्ति: कलांशेन यः पुमांस्त॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 31.7568)
- **Original**: स्वयं प्रकृतिरूपथ्ल॒ मायया च स्वयं पुमान्‌ । तयो: पर स्वयं शश्वत्‌ त॑ नमामि परात्परम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 31.7569)
- **Original**: स्त्रीपुंनपुंसंसक रूप. यो. विभर्ति _ स्वमायया । स्वयं माया स्वयं मायी यो देवस्तं नमाम्यहम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 31.7570)
- **Original**: सर्वदुःखानां सर्वकारणकारणम्‌ । धारणं सर्वविश्वानां सर्ववीज॑ नमाम्यहम्‌
- **Translation**: 

---

