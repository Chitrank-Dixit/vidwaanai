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

### Verse 1 (Vaivtpuran 55.19176)
- **Original**: क्षीरोंदे सिन्धुकन्या क्व मर्त्य लक्ष्मीईरिप्रिया
- **Translation**: 

---

### Verse 2 (Vaivtpuran 55.19177)
- **Original**: सर्वस्वर्गे स्वर्गलक्ष्मीदेवदु:ःखविनाशिनी । सनातनी विष्णुमाया दुर्गा शंकरवक्षसि
- **Translation**: 

---

### Verse 3 (Vaivtpuran 55.19178)
- **Original**: सावित्री वेदमाता च कलया ब्रह्मवक्षस । कलया धर्मपत्ती त्त॑ नरनारायणप्रसू:
- **Translation**: 

---

### Verse 4 (Vaivtpuran 55.19179)
- **Original**: कलया तुलसी त्वं च॒ गड्डा भुवनपावनी । लोमकूपोद्धवा गोप्य:ः कलांशा रोहिणी रति:
- **Translation**: 

---

### Verse 5 (Vaivtpuran 55.19180)
- **Original**: कलाकलांशरूपा च शतरूपा शची दितिः
- **Translation**: 

---

### Verse 6 (Vaivtpuran 55.19181)
- **Original**: अदितिर्देवमाता च त्वत्कलांशा हरिप्रिया
- **Translation**: 

---

### Verse 7 (Vaivtpuran 55.19182)
- **Original**: देव्यक्ष मुनिपल्यक्ष त्वत्कलाकलया शुभे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 55.19183)
- **Original**: कृष्णभक्ति कृष्णदास्य॑ देहि में कृष्णपूजिते
- **Translation**: 

---

### Verse 9 (Vaivtpuran 55.19184)
- **Original**: एवं कृत्वा परीहार॑ स्तुत्वा चर कवच पठेत्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 55.19185)
- **Original**: पुरा कृतं स्तोत्रमेतद्‌ भक्तिदास्वप्रद॑ शुभम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 55.19186)
- **Original**: इति श्रीब्रह्मवैवर्ते श्रीराधाया: परीहारस्तोत्रं सम्पूर्णम्‌। (प्रकृतिखण्ड 55। 44--57 ) जी 4ऑरफसय:+0+0ूर श्रीकृष्णकृतं श्रीराधास्तोत्रम्‌ श्रीकृष्ण उवाच एबमेब प्रियोहह॑ ते प्रमोदक्लव ते मयि । सुव्यक्तम्य कापट्यमचन॑ ते वबरानने
- **Translation**: 

---

### Verse 12 (Vaivtpuran 55.19187)
- **Original**: है कृष्ण त्वं मम॒ प्राणा जीवात्मेति चर संततम्‌। ब्रूषे नित्य तु यत्‌ प्रेम्णा साम्प्रतं तद्‌ गत ड्रतम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 55.19188)
- **Original**: अस्मार्क बचन॑ सत्यं यद्‌ ब्रवीमीति तद्‌ ध्रुवम्‌ । पद्षप्राणाधिदेवी त्व॑ राधा प्राणाधिकेति मे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 55.19189)
- **Original**: शक्तो न रक्षितुं त्वां च यान्ति प्राणास्त्वया विना। विनाधिष्ठातृदेवीं च को वा कुत्र च जीवति
- **Translation**: 

---

### Verse 15 (Vaivtpuran 55.19190)
- **Original**: महाविष्णोश्ष॒ माता त्व॑ मूलप्रकृतिरीक्षीी । सगुणा त्व॑ं च कलबया निर्गुणा स्ववमेव तु
- **Translation**: 

---

### Verse 16 (Vaivtpuran 55.19191)
- **Original**: ज्योतीरूपा निराकारा भक्तानुग्रहविग्रहा। भक्तानां रुचिवैचित्र्यान्नानामूर्ती्ष॒ बिभ्रती
- **Translation**: 

---

### Verse 17 (Vaivtpuran 55.19192)
- **Original**: महालक्ष्मीश्र॒ बैकुण्ठे भारती चर सतां प्रसू:
- **Translation**: 

---

### Verse 18 (Vaivtpuran 55.19193)
- **Original**: पुण्यक्षेत्रे भारते च सती त्बं॑ पार्वती तथा
- **Translation**: 

---

### Verse 19 (Vaivtpuran 55.19194)
- **Original**: तुलसी पुण्यरूपा चर गड्डा भुवनपावनी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 55.19195)
- **Original**: ब्रहालोके क्र सावित्री कलया त्व॑ वसुन्धरा
- **Translation**: 

---

