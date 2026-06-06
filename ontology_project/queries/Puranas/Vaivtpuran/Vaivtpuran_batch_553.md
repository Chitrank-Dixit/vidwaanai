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

### Verse 1 (Vaivtpuran 38.18296)
- **Original**: कारागारे विपदग्रस्त: स्तोत्रेण मुच्यते श्रुवम्‌ । रोगातू प्रमुच्यते रोगी वर्ष श्रुत्वा तु संयत:
- **Translation**: 

---

### Verse 2 (Vaivtpuran 38.18297)
- **Original**: इति ज्रीब्रह्मवैवर्ते नारयणकृतं अ्रीकृष्णस्तोत्रं सम्पूर्णम्‌। (बरह्यखण्ड 3। 10-17) 04000 >स्पेसथेस 2 2र>
- **Translation**: 

---

### Verse 3 (Vaivtpuran 39.8081)
- **Original**: 380 » संक्षिप्त ब्रह्मवैवर्तपुराण « #%ऋ####%#%##%#######%##%####%###%#/#### # कफ ्््क्ऋ्ऋ््््ऋककक पक के वत्स ! इस प्रकार मैंने तुम्हें यह 'ब्रह्मण्डविजय'
- **Translation**: 

---

### Verse 4 (Vaivtpuran 39.8082)
- **Original**: गलेमें अथवा दाहिनी भुजापर धारण करता है, नामक कवच बतला दिया। यह परम अद्भुत
- **Translation**: 

---

### Verse 5 (Vaivtpuran 39.8083)
- **Original**: वह सम्पूर्ण शत्रुओंका मर्दन करनेवाला तथा तथा सम्पूर्ण मन्त्र-समुदायका मूर्तिमान्‌ स्वरूप
- **Translation**: 

---

### Verse 6 (Vaivtpuran 39.8084)
- **Original**: त्रिलोकबिजयी होता है। जो इस कवचको न है। ,समस्त तीर्थोंमें भलीभाँति गोता लगानेसे,
- **Translation**: 

---

### Verse 7 (Vaivtpuran 39.8085)
- **Original**: जानकर दुर्गतिनाशिनी दुर्गाका भजन करता है, सम्पूर्ण यज्ञोंका अनुष्ठान करनेसे तथा सभी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 39.8086)
- **Original**: उसके लिये एक करोड़ जप करनेपर भी मन्त्र प्रकारके ब्रतोपवास करनेसे जो फल प्राप्त होता
- **Translation**: 

---

### Verse 9 (Vaivtpuran 39.8087)
- **Original**: सिद्धिदायक नहीं होता। नारद! यह काण्वशाखोक्त है, वह फल मनुष्य इस कवचके धारण करनेसे
- **Translation**: 

---

### Verse 10 (Vaivtpuran 39.8088)
- **Original**: सुन्दर कबच, जिसका मैंने वर्णन किया है, परम पा लेता है। जो विधिपूर्वक वस्त्र, अलंकार
- **Translation**: 

---

### Verse 11 (Vaivtpuran 39.8089)
- **Original**: गोपनीय तथा अत्यन्त दुर्लभ है। इसे जिस और चन्दनसे गुरुकी पूजा करके इस कवचकों
- **Translation**: 

---

### Verse 12 (Vaivtpuran 39.8090)
- **Original**: किसीको नहीं देना चाहिये।* (अध्याय 39) हल लटक 225.00000 * नारायण उवाच- श्रेणु नारद वक्ष्यामि दुर्गाया: कवच॑ शुभम्‌ । श्रीकृष्णेनेव यददत्त गोलोके ब्रह्मणे पुरा
- **Translation**: 

---

### Verse 13 (Vaivtpuran 39.8091)
- **Original**: ब्रह्मा त्िपुरसंग्रामो शंकाय ददौ. पुरा । जघान त्रिपुरं रुद्रों यद्‌ धृत्वा भक्तिपूर्वकम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 39.8092)
- **Original**: हरो ददी गौतमाय पद्याक्षाय च गौतम: । यतो बधभूव पद्माक्ष: साद्वीपेश्रो जयी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 39.8093)
- **Original**: यदू्‌ धृत्वा पठनाद ब्रह्मा ज्ञानवान्‌ शक्तिमानू भुवि
- **Translation**: 

---

### Verse 16 (Vaivtpuran 39.8094)
- **Original**: शिवों बभूव सर्वज्ञो योगिनां च गुरुर्यतः। शिवतुल्यो गौतम बभूव मुनिसत्तम:
- **Translation**: 

---

### Verse 17 (Vaivtpuran 39.8095)
- **Original**: ब्रह्माण्डविजयस्यास्य कवचस्य॒ प्रजापति: । ऋषिश्छन्द्श गायत्री देवी दुर्गतिनाशिनी
- **Translation**: 

---

### Verse 18 (Vaivtpuran 39.8096)
- **Original**: ब्रह्मण्डविजये. चैब.. बिनियोग: प्रकौर्तित:
- **Translation**: 

---

### Verse 19 (Vaivtpuran 39.8097)
- **Original**: पुण्यतीर्थ च महेतां कवच॑ परमाद्भधतम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 39.8098)
- **Original**: 3 ही दुर्गतिनाशिनयै स्वाहा में पातु मस्तकम्‌
- **Translation**: 

---

