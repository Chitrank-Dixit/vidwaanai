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

### Verse 1 (Vaivtpuran 67.18078)
- **Original**: 3* हीं श्रीं क्‍्लीं कालिकायै स्वाह्म पे पातु मस्तकम्‌ । क्लीं कपालं सदा पातु हीं हीं ढ्लीमिति लोचने
- **Translation**: 

---

### Verse 2 (Vaivtpuran 67.18079)
- **Original**: 3* ह्रीं त्रिलोचने स्वाहा नासिकां मे सदावतु
- **Translation**: 

---

### Verse 3 (Vaivtpuran 67.18080)
- **Original**: क्लीं कालिके रक्ष रक्ष स्वाहा दन्तं सदाबतु
- **Translation**: 

---

### Verse 4 (Vaivtpuran 67.18081)
- **Original**: हुं भद्दकालिके स्वाहा पातु मे5धरयुग्मकम्‌ । 30 हीं हीं क्‍्लीं कालिकायै स्वाहा कण्ठं सदावतु
- **Translation**: 

---

### Verse 5 (Vaivtpuran 67.18082)
- **Original**: 3» ह्वीं कालिकायै स्वाहा कर्णयुग्म॑ सदावतु । 30 क्री क्रीं ब्लीं काल्यै स्वाहा स्कन्धं पातु सदा मम
- **Translation**: 

---

### Verse 6 (Vaivtpuran 67.18889)
- **Original**: » श्रीकृष्णस्तोज्राणि « 825 क्ऋड़कऋ ऋऋकऋड़ कक कक ऋकऋ ऋऋऋऋकऋ कर ऋऋ ऋऋ #ऋऋ%$%$%ऊऋ%ऊकऊऋऋ%ऊऋ%ऊऋऊऋऋ%$%%%%$%%%%%4$%$% 59% 4 # # 'अननिनननननननननननननननननननननननननननन मनन मनन न न नननिनननिननियनिनिनितिनिलिनियनययणनियणनणययण।य-यययण+॑+++ “7-7 777“7“+7+7+707108--- 77? 0-0_?1+ - - - -#77/ 77 राधाकृतं श्रीकृष्णस्तवनम्‌ राधिकोबाच प्रफुल्लाहं त्वया नाथ मृता म्लाना च त्वां बिना । यथा महौषधिगण: प्रभाते भाति भास्करे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 67.18890)
- **Original**: नक्त दीपशिखेवाहं त्वया सार्थ त्वया विना । दिने दिने यथा क्षीणा कृष्णपक्षे विधो: कला
- **Translation**: 

---

### Verse 8 (Vaivtpuran 67.18891)
- **Original**: तब वक्षसि में दीप्ति: पूर्णचन्द्रप्रभासमा। सद्यो मृता त्वया त्यक्ता कुट्डां चन्द्रकला यथा
- **Translation**: 

---

### Verse 9 (Vaivtpuran 67.18892)
- **Original**: ज्वलदग्रिशिखेवाह॑ घृताहुत्या त्ववा सह । त्वया विनाहं निर्वाणा शिशिरे पद्चिनी यथा
- **Translation**: 

---

### Verse 10 (Vaivtpuran 67.18893)
- **Original**: चिन्ताज्वरजराग्रस्ता मत्तस्त्वयि गतेउप्यहम्‌ । अस्तं॑ गते रवौ चन्द्रे ध्वान्तग्रस्ता थरा यथा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 67.18894)
- **Original**: भ्रष्टो वेषस्त्वां बिना मे रूपं यौवनचेतनम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 67.18895)
- **Original**: तारावली . परिभ्रष्टा. सूर्यसूतोदये.. यथा
- **Translation**: 

---

### Verse 13 (Vaivtpuran 67.18896)
- **Original**: त्वमेबात्मा च सर्वेषां मम नाथो विशेषत: । तनुर्यथा55त्मना त्यक्ता तथाहं चत्र त्वया बिना
- **Translation**: 

---

### Verse 14 (Vaivtpuran 67.18897)
- **Original**: पदञ्ञप्राणात्मकस्त्व॑ में मृताईं च त्वया विना । दृष्टेआ गोलकौ यद्दद्‌ दृष्टिपुत्तलिकां विना
- **Translation**: 

---

### Verse 15 (Vaivtpuran 67.18898)
- **Original**: स्थल यथा चित्रयुक्त त्वया सार्धमहं तथा । असंस्कृता त्वया हीना तृणच्छन्ना यथा मही
- **Translation**: 

---

### Verse 16 (Vaivtpuran 67.18899)
- **Original**: त्वया सार्थमहं कृष्ण चित्रयुक्तेव मृण्मयी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 67.18900)
- **Original**: त्वां विना जलधौताहं विरूपा मृण्मयीव च
- **Translation**: 

---

### Verse 18 (Vaivtpuran 67.18901)
- **Original**: गोपाड्ुनानां शोभा च त्वया रासेश्वेण च । हारे स्वर्णविकारे चर श्रेतेत मणिना सह
- **Translation**: 

---

### Verse 19 (Vaivtpuran 67.18902)
- **Original**: च्रजराज त्वया सार्थ राजन्ते राजराजय:
- **Translation**: 

---

### Verse 20 (Vaivtpuran 67.18903)
- **Original**: यथा चनद्रेण नभसि ताराराजिर्विराजते
- **Translation**: 

---

