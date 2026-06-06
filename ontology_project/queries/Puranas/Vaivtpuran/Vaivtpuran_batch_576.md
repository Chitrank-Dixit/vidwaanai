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

### Verse 1 (Vaivtpuran 44.17854)
- **Original**: हर्षमड्नलदक्षे ता हर्षमड्जलचण्डिके । शुभे मड्डलदक्षे च शुभमड्डलचण्डिके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 44.17855)
- **Original**: मड़ले मड़लाहें च सर्वमड्रलमड्रले । सतां मड्लदे देवि सर्वेषां मड्जडलालये
- **Translation**: 

---

### Verse 3 (Vaivtpuran 44.17856)
- **Original**: पूम्या मड्रलबवारे च गड़लाभीष्टदैवते । पूज्ये मड्गलभूपस्थ मनुवंशस्थ संततम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 44.17857)
- **Original**: मड्ुलाधिष्ठावदेवि. मड्डलानां च मड्जले । संसारमड्ललाधारे मोक्षमड्रलदायिनि
- **Translation**: 

---

### Verse 5 (Vaivtpuran 44.17858)
- **Original**: सारे च मड्डलाधारे पारे च सर्वकर्मणाम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 44.17859)
- **Original**: प्रतिमड्डलवारें च पूज्ये च मड्जनलप्रदे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 44.17860)
- **Original**: स्तोग्रेणानेन शब्भुश्च स्तुत्वा मड्गडलचण्डिकाम्‌ । प्रतिमड्रलवारे चर पूजां कृत्वा गत: शिव:
- **Translation**: 

---

### Verse 8 (Vaivtpuran 44.17861)
- **Original**: देव्याश्न॒मडूलस्तोत्रं यः श्रृणोति समाहित: । तन्मड्रल॑ भवेच्छश्नत्न॒ भवेत्‌_ तदमड्ुलम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 44.17862)
- **Original**: इति #ब्रह्मवैवर्ते मन्त्रध्यानसहितं मड़लचण्डिकास्तोत्र सम्पूर्णप्‌ / ( प्रकृतिखण्ड 44
- **Translation**: 

---

### Verse 10 (Vaivtpuran 44.17863)
- **Original**: 20--36) # हब कर 200/-0050 श्रीकृष्णकृतं दुर्गास्तोत्रम्‌ श्रीकृष्ण उवाच त्वमेव सर्वजननी . मूलप्रकृतिरीश्वरी । त्वमेवाद्या सृष्टिविधौ स्वेच्छवा त्रिगुणात्मिका
- **Translation**: 

---

### Verse 11 (Vaivtpuran 44.17864)
- **Original**: कार्यार्थे सगुणा त्वं च बस्तुतो निर्गुणा स्वयम्‌ । परश्रह्मस्वरूपा त्व॑ सत्या नित्या सनातनी
- **Translation**: 

---

### Verse 12 (Vaivtpuran 44.17865)
- **Original**: तेजःस्वरूणा परमा भक्तानुग्रहविग्रहा । सर्वस्वरूपा सर्वेशा सर्वाधारा परात्परा
- **Translation**: 

---

### Verse 13 (Vaivtpuran 44.17866)
- **Original**: सर्वबीजस्वरूपा च सर्वपूज्या निराश्रया । सर्वज्ञा सर्वतोभद्रा सर्वमड्गलमड्रला
- **Translation**: 

---

### Verse 14 (Vaivtpuran 44.17867)
- **Original**: सर्ववुद्धिवरूपा च सर्वशक्तिस्वरूपिणी । सर्वज्ञानप्रदा देवी सर्वज्ञा सर्वभाविनी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 44.17868)
- **Original**: त्व॑ं स्वाहा देवदाने च पितृदाने स्वधा स्वयम्‌ । दक्षिणा सर्वदानें च सर्वशक्तिस्वरूपिणी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 44.17869)
- **Original**: निद्रा त्वं च दया त्वं च तृष्णा त्व॑ चात्मन: प्रिया । क्षुत्क्षान्ति: शान्तिरीशा च कान्तिः सृष्टिश्न शाश्वती
- **Translation**: 

---

### Verse 17 (Vaivtpuran 45.4397)
- **Original**: * प्रकृतिखण्ड « 239 अऋऋऋऋ 4422 %######$#%#%%%%%% 55%; #
- **Translation**: 

---

### Verse 18 (Vaivtpuran 45.4398)
- **Original**: # ######### ###### कक गोपीपति परम प्रभु उन परमेश्वरने इनके वस्त्र
- **Translation**: 

---

### Verse 19 (Vaivtpuran 45.4399)
- **Original**: करता है। जो पुरुष पूजाके समय इन बारह और शरीरको जीर्ण देखकर इनका “जरत्कारु'
- **Translation**: 

---

### Verse 20 (Vaivtpuran 45.4400)
- **Original**: नामोंका पाठ करता है, उसे तथा उसके बंशजको नाम रख दिया। साथ ही, उन कृपानिधिने
- **Translation**: 

---

