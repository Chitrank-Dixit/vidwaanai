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

### Verse 1 (Vaivtpuran 31.19148)
- **Original**: ऊर्ध्व नारायण: पातु ह्वाथस्तात्‌ कमलापतिः । पूर्वस्यां पातु गोपाल: पातु बह्नौ दशास्यहा
- **Translation**: 

---

### Verse 2 (Vaivtpuran 31.19149)
- **Original**: वनमाली पातु याम्वां बैकुण्ठः पातु नै््रतौ । बारुण्यां बासुदेवश्ष सतो रक्षाकरः: स्वयम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 31.19150)
- **Original**: पातु ते संततमजो वायव्यां विष्टरश्रवा:
- **Translation**: 

---

### Verse 4 (Vaivtpuran 31.19151)
- **Original**: उत्ते च सदा पातु तेजसा जलजासन:
- **Translation**: 

---

### Verse 5 (Vaivtpuran 31.19152)
- **Original**: ऐशान्यामीश्वर: पातु सर्वत्र पातु शत्रुजित्‌ । जले स्थले चान्तरिक्षे निद्रायां पातु राघव:
- **Translation**: 

---

### Verse 6 (Vaivtpuran 31.19153)
- **Original**: इत्येब॑ कथितं ब्रह्मनू कबच॑ परमाद्धुतम्‌ । कृष्णेन कृपया दत्त॑ स्मृतेनेव पुरा मया
- **Translation**: 

---

### Verse 7 (Vaivtpuran 31.19154)
- **Original**: शुम्भेन सह संग्रामे निर्लक्ष्ये घोरदारुणे । गगने स्थितया सह्या: प्राप्तिमात्रेण सो जित:
- **Translation**: 

---

### Verse 8 (Vaivtpuran 31.19155)
- **Original**: कवचस्य॒प्रभावेण धरण्यां पतितो मृत:
- **Translation**: 

---

### Verse 9 (Vaivtpuran 31.19156)
- **Original**: पूर्व वर्षशतं खे च कृत्वा युद्ध॑ भयावहम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 31.19157)
- **Original**: मृते शुम्भे च गोविन्द: कृपालुर्गगनस्थित: । माल्यं च कबचं दत्त्वा गोलोकं॑ स जगाम ह
- **Translation**: 

---

### Verse 11 (Vaivtpuran 31.19158)
- **Original**: कल्पान्तरस्यतवृत्तान्त॑ कृपया कथित मुने । अध्यन्तभर्य नास्ति कबचस्यथ॒ प्रभावत:
- **Translation**: 

---

### Verse 12 (Vaivtpuran 31.19159)
- **Original**: कोटिशः कोटिशो नष्टा मया दृष्टाश्ष वेधसः । अहं च हरिणा सार्ध कल्पे कल्पे स्थिरा सदा
- **Translation**: 

---

### Verse 13 (Vaivtpuran 31.19160)
- **Original**: इत्युक्वा कवचं दत्त्वा सान्तर्थानं चकार ह। निःशद्लों नाभिकमले तस्थौँ स कमलोद्धव:
- **Translation**: 

---

### Verse 14 (Vaivtpuran 31.19161)
- **Original**: सुबर्णगुटिकायां तु कृत्वेंदे कवचत्न॑ परम्‌ । कण्ठे वा दक्षिणे बाहौँ बध्नीयाद्‌ यः सुथी: सदा
- **Translation**: 

---

### Verse 15 (Vaivtpuran 31.19162)
- **Original**: विषाग्रिसर्पशत्रुभ्पो भय तस्य न विद्यते । जले स्थले चान्तरिक्षे निद्रायां रक्षतीश्वरः
- **Translation**: 

---

### Verse 16 (Vaivtpuran 31.19163)
- **Original**: डति औन्रह्मवैवर्ते ब्रह्मार्ण प्रति योगनिद्रयोपदिष्टं श्रीकृष्णकवर्च सम्पूर्णम्‌। ( श्रोकृष्णजन्मखण्ड 12। 17--36) #न्‍टां/8आ 9044 :0000047
- **Translation**: 

---

### Verse 17 (Vaivtpuran 32.7593)
- **Original**: 362 + संक्षिप्त ब्रह्मवैवर्तपुराण * ह. ) +
- **Translation**: 

---

### Verse 18 (Vaivtpuran 32.7594)
- **Original**: ]. ] %%%#%%%#%##########$%%ऋऋ%ऋऋ##########क#ऊकऋऊऋऊऋऊकऋऊऋऊऋऋऊऋऋ
- **Translation**: 

---

### Verse 19 (Vaivtpuran 32.7595)
- **Original**: ऋ ; 446 #######%#ऋ%%$%%$%% पुष्करमें जाकर परशुरामका तपस्या करना, श्रीकृष्णद्वारा बर-प्राप्ति, आभ्रमपर मित्रोंक साथ उनका विजय-यात्रा करना और शुभ शकुनोंका प्रकट होना, नर्मदातटपर रात्रिमें परशुरामको स्वप्रमें शुभ शकुनोंका दिखलायी देना श्रीनारायण कहते हैं--नास्द! तदनन्तर
- **Translation**: 

---

### Verse 20 (Vaivtpuran 32.7596)
- **Original**: विमान दीख पड़ा, जिसपर एक अत्यन्त सुन्दर भूगुवंशी परशुराम हर्षपूर्वक शिव, दुर्गा तथा
- **Translation**: 

---

