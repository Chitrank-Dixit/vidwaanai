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

### Verse 1 (Vishnu Puran 0.6381)
- **Original**: कृशाश्वके सोमदत्त नामक पुत्र हुआ, जिसने सौ अश्वमेध-यज्ञ किये थे। उससे जनमेजय हुआ और जनमेजयसे सुमतिका जन्प हुआ। ये सब विशालवंजशोय राजा हुए। इनके विषयमें यह इलोक प्रसिद्ध है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6382)
- **Original**: 576--60
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6383)
- **Original**: *तृणबिन्दुके प्रसादसे विशालवंशीय समस्त राजाछोग दीर्घायु, महात्मा, वीर्यवान्‌ और अति धर्मपरायण हुए
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6384)
- **Original**: मनुपुत्र दार्यातिके सुकन्या नामवाली एक कन्या हुई, जिसका विवाह व्यवन ऋषिके साथ हुआ
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6385)
- **Original**: जर्यातिके आनर्त्त नामक एक परम धार्मिक पुत्र हुमा। आनरत्तेंके रेवत नामका पुत्र हुआ जिसने कुशस्थल्त नामकी पूरीमें रहकर आनर््तदेशका एज्यभोग किया
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6386)
- **Original**: शैवतका भी रैवत ककुद्यी नामक एक अति धर्मात्मा पुत्र था, जो अपने सौ भाइयोंमें सबसे बड़ा था
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6387)
- **Original**: उसके रेबती नामको एक कन्या हुई
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6388)
- **Original**: महाराज रैवत उसे अपने साथ लेकर ब्रह्माजीसे यह पूछनेके लिये कि 'यह कन्या किस बस्के योग्य है' बह्मल्प्ेककों गये
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6389)
- **Original**: उस समय कऋष्माजीके समीप हाहम और हूहू नामक दो गन्धर्व अतितान नामंक दिव्य गान गा रहे थे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6390)
- **Original**: जहाँ [गान-सम्बस्धी चित्रा, दक्षिणा और धात्री नामक] त्रिमार्गके परिवर्तनके साथ उनका विलक्षण गान खुनते हुए अनेकों युगोंके परिवर्तन-कालतक ठहस्नेपर भी रैवतजीको केवल एक मुहूर्त ही बोता-सा मालूम हुआ
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6391)
- **Original**: गान समाप्त हो जानेपर रैबतने भगवान्‌ कमलयोनिको
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6392)
- **Original**: र्े0 ओविष्णुप्राण (अः 2 कन्वायोम्य॑ वरमपृच्छत्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6393)
- **Original**: ततश्चासौ भगवानकथयत्‌ कथय योउभिमतस्ते वर डइति
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6394)
- **Original**: पुनश्च प्रणम्थ भगवते तस्मै यथाभि- मतानात्मनस्स वरान्‌ू कथयामास। क एपवां भगवतो5भिमत ड्ति यस्मै कन्यामिमां प्रयच्छा- प्रीति
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6395)
- **Original**: ततः किजखझिदवनतशिरास्सस्मितं भगवानब्ज- योनिराह
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6396)
- **Original**: य एते भवतोउभिमता नैतेषां साम्प्रत॑ पुत्रपौत्रापत्यापत्यसन्ततिरस््थववनीतले
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6397)
- **Original**: बहुनि तवात्रैव गाल्थर्व॑ शृण्वत- अ्तुर्युगान्यतीतानि
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6398)
- **Original**: साम्पत॑ महीतले- इष्टाविंशतितममनोश्रतुर्युगमतीतप्राय॑ वर्तते
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6399)
- **Original**: आसत्नो हि कलिः
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6400)
- **Original**: अन्यस्मे कन्यारब्रपिदं भवतैकाकिनाभिमताय _देयम्‌
- **Translation**: 

---

