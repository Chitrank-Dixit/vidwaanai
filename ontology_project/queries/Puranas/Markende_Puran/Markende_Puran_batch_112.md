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

### Verse 1 (Markende Puran 0.2221)
- **Original**: इस प्रकार धोखेमें आ जानेपर जब उन्होंने सम्पूर्ण जगतूपें जल ही- जल टेखा तब कमलगयन भगधानसे कहा--' जहाँ । पृथ्त्रो जलपें डूबी हुई ते हो--जहाँ सूखा स्थान हो, वहीं हमारा वध करों '
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2222)
- **Original**: 100-101
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2223)
- **Original**: ज्ष्ठिकाच 11024 कश्नेत्युक्लला भगवता शबद्भुच॒क्तगदाभृता। कृत्या चक्रेण वै च्छिने जधने शिरसी तयो:
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2224)
- **Original**: ग्रभावमस्यादेव्यास्तु भूष: श्ृणु बदापि ते हऐं 33
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2225)
- **Original**: ऋषिकहते हैं --
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2226)
- **Original**: तब्र ' तथास्तु "कहकर शह्छू, चक्र और गदा धारण करनेवाले भगबानने उन दोनोंके मस्तक अपनी जाँघपर रखकर चक्रसे काट डाले
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2227)
- **Original**: इस प्रकार ये देवो महागाया ज्ह्माजीकी स्तुति करनेपर स्ववं प्रकट हुईं थीं। अब पुनः तुपसे उनके प्रभाबका वर्णन करता हूँ, सुनो
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2228)
- **Original**: 103-104
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2229)
- **Original**: हेशि औपार्फण्डेबयुराणे स्ाकापिके गलतसरे देवीफहत्म्पे प्रधुक्नैटसब्ों काम प्रथमोरउ ध्शाय: # 2
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2230)
- **Original**: गकछाच 14 अद्धाशलौका: 20, शलोकाः 64, एवम
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2231)
- **Original**: इस प्रकार श्रीमार्कण्डेयंपुराणमें सावर्णिक्र मन्त्रन्तरकी कथाके अन्तर्गत वेबीमाहात्म्यमें 'मधु-कैटभ-बध्न' नामक पहला अध्याय पूरा हुआ
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2232)
- **Original**: #>€गसि#्फिटिटज+ 0 अध्कि पाट है [ 5539 ] सं0 मार घु0--7 6. प0- यता। +.
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2233)
- **Original**: $0148यणुराणवों कई इतियोंप यहाँ ग्रीन स्वस्तव थ्रुद्धेन श्लाघ्यसस्यं एत्युरानयो: :' इटज
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2234)
- **Original**: 186 44444 उय:त:4 92757 7744 656::::72 77255 0 “संक्षिप्त मार्कण्डेयपुराण * (3074 46/5 4 #ै&
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2235)
- **Original**: 55% 76 722.20.25770 684 6:64 77222 # 7 द्वितीयो5उथ्याय: देवताओंके तेजसे देवीका प्रादर्भाव और महिषासुरकी सेनाका वध बिनियोग सशधादृत्त॑ 'तयोस्तटून्महिषासुरचेष्टितम्‌
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2236)
- **Original**: 3» परध्यपचरित्रस्य विष्णुत्ैषिमंहालक्ष्मीदेवता,
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2237)
- **Original**: ज़िदशा:_ कथयाघमासुर्देवाभिभवतिस्तरम्‌
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2238)
- **Original**: उष्णिक्‌ छन्दः, शाकम्भरी शक्ति:; दुर्गा जीजम, वायुस्तत्त्वपू, यजुर्वेद्‌: स्वरूपम, श्रीमहाल ह्ष्मीप्रीत्यर्थ प्रध्यमचरित्रजपे विभियोगः। 55 मध्यम अरित्रके विप्णु ऋषि, महालक्ष्मी देवता, उश्णिक कद, शाकम्भरी शक्ति, दुर्गा बीज, वायु तक्त और यजुर्वेद स्वरूप है। श्रीमहालक्ष्मीको प्रसशताके लिये मध्यम चरित्रके पाठसें इसका विनियोग है। ध्यान 30 अक्षस्नक्परशु गदेबुकुलिश पर्व धनुष्कुण्डिकां दण्ड शक्तिमसिं च चर्म जलजं घण्टां सुगभाजनप््‌ शूल॑ पाशसुदर्शने च दअतती हंस्तैः प्रवालप्रभां सेजे सैरिभमर्दिनीमिह ग्रहाल्क्ष्मीं सरोजस्थिताम्‌
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2239)
- **Original**: मैं कमलके आसनपर नबैठी हुई पहिषासुरमर्दिनों भगथती महालक्ष्यीका भजन करता हूँ, जो अपने हाथोंमें अक्षमाला, फरसा, गदा, बाण, वज्र, पद्म, धनुष, कण्डिका, दण्ड, शक्ति, खड़, ढाल, शंख, प्रण्टा, मधुपात्र, शुल, पाश और चक्र पारण करता हैं तथा जिनके श्रोविग्रहक्तों कान्ति मूँगेके फरमान लाल है।] “35 ही" ऋषिरुवान 46 / देवासुरपभ्ुझ्ुद्धं/ पूर्णमब्दशत पुरा। सूर्ेद्धाग्न्यनिलेन्दूनां यमस्य वहणस्य ञञ। अन्येषां चाधिकाग़न्‌ स॒ स्वयपेत्राधितिध्र॒ति
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2240)
- **Original**: स्वर्गान्निराकृता: सर्वे तेम देखंगणा भुवि। विचरन्ति यथा मर्न्या महिषरेण दुरात्मना
- **Translation**: 

---

