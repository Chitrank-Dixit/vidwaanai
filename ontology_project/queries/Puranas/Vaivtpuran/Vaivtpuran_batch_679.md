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

### Verse 1 (Vaivtpuran 75.9228)
- **Original**: व्याधि, भय और यमयातना--ये सारे कष्ट दूसरे-
- **Translation**: 

---

### Verse 2 (Vaivtpuran 88.18023)
- **Original**: « श्रीदुर्गास्तोत्राणि * 795 #%#88%%&#8##%#%#&##%### ## ######&############%&##6%#%#############&# 6668 ##6## 66% 6#%# 4 ##ऋ # त्व॑ च्॒ ब्रह्मदिदेवानामम्बिके जगदम्बिके । मायया पुरुषस्त्व॑ च्र मायया प्रकृतिः स्वयम्‌ । बेदानां जननी त्वं च सावित्री च परात्परा । मर्त्यलक्ष्मीक क्षीरोदे कामिनी शेषशायिन: । नागादिलक्ष्मी: पाताले गृहेषु गृहदेवता । रागाधिष्ठातृदेवी त्व॑ ब्रह्मणश्च॒ सरस्वती । गोलोके चर स्वयं राधा श्रीकृष्णस्यैव वक्षसि । श्रीरासमण्डले. रम्या वृन्दावनविनोदिनी । दक्षकन्या कुत्र कल्पे कुत्र कल्पे च शैलजा । त्वमेव गड्डा तुलसी त्व॑ च स्वाहा स्वधा सती । स्त्रीरूपं चापिपुरुषं देवि त्व॑ च नपुंसकम्‌ । वह्हौँ च दाहिकाशक्तिर्जले शैत्यस्वरूपिणी । गन्धरूपा च भूमौ च आकाशे शब्दरूपिणी । सृष्टी सृष्टिस्वरूपा च पालने परिपालिका । क्षुत्त्यं दया त्वं निद्रा त्वं तृष्णा त्य॑ बुस्द्ररपिणी । शान्तिस्त्यं च स्वयं भ्रान्ति: कान्तिस्त्वं कीर्तिरेव च । त्व॑ साकारे च गुणतो निराकारे चर निर्गुणात्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 88.18024)
- **Original**: त़यो: पर ब्रह्म पर॑ त्यं बिभर्षि सनातनि
- **Translation**: 

---

### Verse 4 (Vaivtpuran 88.18025)
- **Original**: बैकुण्ठे च महालक्ष्मी: सर्वसम्पत्स्वरूपिणी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 88.18026)
- **Original**: स्वर्गेषु स्वर्गलक्ष्मीस्त्व॑ राजलक्ष्मीक्ष भूतले
- **Translation**: 

---

### Verse 6 (Vaivtpuran 88.18027)
- **Original**: सर्वशस्यस्वरूपा._त्व॑ सर्वैश्वर्यविधायिनी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 88.18028)
- **Original**: प्राणानामधिदेवी त्व॑ कृष्णस्थ परमात्मन:
- **Translation**: 

---

### Verse 8 (Vaivtpuran 88.18029)
- **Original**: गोलोकाथिष्ठिता देवी बृन्दावनवने बने
- **Translation**: 

---

### Verse 9 (Vaivtpuran 88.18030)
- **Original**: शतशभ्ृड्राधिदेवी त्वं नाप्ना चित्रावलीति च
- **Translation**: 

---

### Verse 10 (Vaivtpuran 88.18031)
- **Original**: देवमातादितिस्त्व॑ च॒ सर्वाधारा वसुन्धरा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 88.18032)
- **Original**: त्वदंशांशांशकलया सर्वदेवादियोषित:
- **Translation**: 

---

### Verse 12 (Vaivtpuran 88.18033)
- **Original**: यृक्षाणां वृक्षरूपा त्वं सृष्टा चाद्भूररूपिणी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 88.18034)
- **Original**: सूर्य तेज:स्वरूपा च प्रभारूपा च संततम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 88.18035)
- **Original**: शोभास्वरूपा चन्द्रे च पद्मससज्भे चर निश्चितम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 88.18036)
- **Original**: महामारी च संहारे जले च॑ जलरूपिणी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 88.18037)
- **Original**: तुष्टिस्त्वं चापि पुष्टिस्त्वं श्रद्धा त्यं च क्षमा स्वयम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 88.18038)
- **Original**: लज्ञा त्वं च तथा माया भुक्तिमुक्तिस्वरूपिणी
- **Translation**: 

---

### Verse 18 (Vaivtpuran 88.18039)
- **Original**: सर्वशक्तिस्वरूपा त्व॑ सर्व॑सम्पत्प्रदायिनी । बेदेउनिर्बचनीया त्व॑ त्वां न जानाति कश्नन
- **Translation**: 

---

### Verse 19 (Vaivtpuran 88.18040)
- **Original**: सहस्तवकत्रस्त्वां स्तोतुंन च शक्त: सुरेश्वरि । वेदा न शक्ता: को विद्वान न च शक्ता सरस्वती
- **Translation**: 

---

### Verse 20 (Vaivtpuran 88.18041)
- **Original**: स्वयं विधाता शक्तो न न च विष्णु: सनातन: । कि. स्तौमि पक्चवक्त्रेण रणगत्रस्तो महेश्चारि
- **Translation**: 

---

